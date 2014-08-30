.. title: strcpy两种写法的看法
.. slug: strcpyliang-chong-xie-fa-de-kan-fa
.. date: 2011-11-08 09:11:16 UTC+08:00
.. tags: C/C++ ,strcpy ,glibc
.. link: 
.. description: strcpy两种写法的看法
.. type: text

源代码直接Copy 见谅
据说这个是GNU的写法（my_strcpy2）

.. code-block:: c
   :number-lines:

    char * 
    my_strcpy2 (dest, src)
         char *dest;
         const char *src;
    {
      register char c;
      char * s = (char *)src;
      const int off = dest - s - 1;
      do{
          c = *s++;
          s[off] = c;
        }while (c != '\0');
      return dest;
    }
    
另外一种写法来自GFree_Wind（my_strcpy1）

.. code-block:: c
   :number-lines:

    char* my_strcpy1(char *dest, const char *src)
    {
        char *d = dest;
        register char c;
        do{
            c = *src++;
            *d++ = c;
        } while ('\0' != c);
        return dest;
    }
    
根据 CFree_Wind 大牛的说法 （本人小菜）1的效率要高于2 详情如下

http://blog.chinaunix.net/space.php?uid=23629988&do=blog&id=2759769

.. TEASER_END

既然大牛说大家都是学习那我使用VS2008 捣鼓了一番

这个是第一种反汇编出来的 为了不影响统计排除了空行和不考虑编译器的优化

.. code-block:: c
   :number-lines:
      
    char* my_strcpy1(char *dest, const char *src)
    {
    004113D0 push ebp
    004113D1 mov ebp,esp
    004113D3 sub esp,0D8h
    004113D9 push ebx
    004113DA push esi
    004113DB push edi
    004113DC lea edi,[ebp-0D8h]
    004113E2 mov ecx,36h
    004113E7 mov eax,0CCCCCCCCh
    004113EC rep stos dword ptr es:[edi]
        char *d = dest;
    004113EE mov eax,dword ptr [dest]
    004113F1 mov dword ptr [d],eax
        register char c;
        do {
            c = *src++;
    004113F4 mov eax,dword ptr [src]
    004113F7 mov cl,byte ptr [eax]
    004113F9 mov byte ptr [c],cl
    004113FC mov edx,dword ptr [src]
    004113FF add edx,1
    00411402 mov dword ptr [src],edx
            *d++ = c;
    00411405 mov eax,dword ptr [d]
    00411408 mov cl,byte ptr [c]
    0041140B mov byte ptr [eax],cl
    0041140D mov edx,dword ptr [d]
    00411410 add edx,1
    00411413 mov dword ptr [d],edx
        } while ('\0' != c);
    00411416 movsx eax,byte ptr [c]
    0041141A test eax,eax
    0041141C jne my_strcpy1+24h (4113F4h)
        return dest;
    0041141E mov eax,dword ptr [dest]
    };
    00411421 pop edi
    00411422 pop esi
    00411423 pop ebx
    00411424 mov esp,ebp
    00411426 pop ebp
    00411427 ret

这个是2种写法的汇编

.. code-block:: c
   :number-lines:

    char * my_strcpy2 (char *dest, const char *src)
    {
    00411440 push ebp
    00411441 mov ebp,esp
    00411443 sub esp,0E4h
    00411449 push ebx
    0041144A push esi
    0041144B push edi
    0041144C lea edi,[ebp-0E4h]
    00411452 mov ecx,39h
    00411457 mov eax,0CCCCCCCCh
    0041145C rep stos dword ptr es:[edi]
        register char c;
        char * s = (char *)src;
    0041145E mov eax,dword ptr [src]
    00411461 mov dword ptr [s],eax
        const int off = dest - s - 1;
    00411464 mov eax,dword ptr [dest]
    00411467 sub eax,dword ptr [s]
    0041146A sub eax,1
    0041146D mov dword ptr [off],eax
        do{
            c = *s++;
    00411470 mov eax,dword ptr [s]
    00411473 mov cl,byte ptr [eax]
    00411475 mov byte ptr [c],cl
    00411478 mov edx,dword ptr [s]
    0041147B add edx,1
    0041147E mov dword ptr [s],edx
            s[off] = c;
    00411481 mov eax,dword ptr [s]
    00411484 add eax,dword ptr [off]
    00411487 mov cl,byte ptr [c]
    0041148A mov byte ptr [eax],cl
        }
        while (c != '\0');
    0041148C movsx eax,byte ptr [c]
    00411490 test eax,eax
    00411492 jne my_strcpy2+30h (411470h)
        return dest;
    00411494 mov eax,dword ptr [dest]
    };
    00411497 pop edi
    00411498 pop esi
    00411499 pop ebx
    0041149A mov esp,ebp
    0041149C pop ebp
    0041149D ret
    

分析：

第一种一共44行代码 第二种 48行代码 如果汇编的代码条数作为算法的效率那么真的是第一种效率高吗？

两段代码最主要的差异在这个位置

.. code-block:: c
   :number-lines:
      
    *d++ = c;
    00411405 mov eax,dword ptr [d]
    00411408 mov cl,byte ptr [c]
    0041140B mov byte ptr [eax],cl
    0041140D mov edx,dword ptr [d]
    00411410 add edx,1
    00411413 mov dword ptr [d],edx

.. code-block:: c
   :number-lines:
      
    s[off] = c;
    00411481 mov eax,dword ptr [s]
    00411484 add eax,dword ptr [off]
    00411487 mov cl,byte ptr [c]
    0041148A mov byte ptr [eax],cl

GNU 在循环里面 少用了 2条汇编指令

不是我崇洋媚外 确实这个地方相当精妙

使用堆栈平行的内存空间来节省 CPU所执行的指令数这个是非常精妙的

虽然我没有进行进一步的实际测试 但是 CFree_Wind 大牛我个人不同意您的说法 

如果循环仅执行一次那么您的效率要高但是如果忽略循环外面的代码影响那么GNU的算法效率是您的

10/12=80%左右

可以断然 如果实际使用中 GNU的算法效率比第一种写法提高了 10%-20%

==========更新补充

着两个代码一个在于使用了offset降低循环次数，但是需要通过计算得来offset数值，另外一段代码在于简洁容易理解。

而效率上基本上没有差别。两种不同的思路而已。
    