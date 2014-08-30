# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409327354.071269
_enable_loop = True
_template_filename = u'themes/test/templates/base_helper.tmpl'
_template_uri = u'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_headstart', 'html_navigation_links', 'html_stylesheets', 'html_translations', 'html_feedlinks']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        colorbox_locales = context.get('colorbox_locales', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>\n            <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer(u'            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>\n            <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>\n')
            else:
                __M_writer(u'            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n')
            __M_writer(u'        <script src="/assets/js/jquery.colorbox-min.js"></script>\n')
        if colorbox_locales[lang]:
            __M_writer(u'        <script src="/assets/js/colorbox-i18n/jquery.colorbox-')
            __M_writer(unicode(colorbox_locales[lang]))
            __M_writer(u'.js"></script>\n')
        __M_writer(u'    ')
        __M_writer(unicode(social_buttons_code))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        description = context.get('description', UNDEFINED)
        title = context.get('title', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer(u"prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer(u'og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer(u'article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer(u'fb: http://ogp.me/ns/fb# ')
            __M_writer(u"'")
        if is_rtl:
            __M_writer(u'dir="rtl" ')
        __M_writer(u'lang="')
        __M_writer(unicode(lang))
        __M_writer(u'">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer(u'    <meta name="description" content="')
            __M_writer(unicode(description))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="viewport" content="width=device-width, initial-scale=1">\n    \n    <title>')
        __M_writer(striphtml(unicode(title)))
        __M_writer(u'</title>\n\n    ')
        __M_writer(unicode(html_stylesheets()))
        __M_writer(u'\n    ')
        __M_writer(unicode(html_feedlinks()))
        __M_writer(u'\n')
        if permalink:
            __M_writer(u'      <link rel="canonical" href="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
        __M_writer(u'\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
        __M_writer(u'\n')
        if comment_system == 'facebook':
            __M_writer(u'        <meta property="fb:app_id" content="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'">\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(mathjax_config))
        __M_writer(u'\n')
        if use_cdn:
            __M_writer(u'        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer(u'        <!--[if lt IE 9]><script src="/assets/js/html5.js"></script><![endif]-->\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer(u'            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">')
                __M_writer(unicode(text))
                __M_writer(u'<b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer(u'                    <li class="active"><a href="')
                        __M_writer(unicode(permalink))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                    else:
                        __M_writer(u'                    <li><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                __M_writer(u'            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer(u'                <li class="active"><a href="')
                    __M_writer(unicode(permalink))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
                else:
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        notes = context.get('notes', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        post = context.get('post', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        annotations = context.get('annotations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer(u'            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer(u'            <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">\n')
            else:
                __M_writer(u'            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer(u'        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(_link("index", None, langname)))
                __M_writer(u'" rel="alternate" hreflang="')
                __M_writer(unicode(langname))
                __M_writer(u'">')
                __M_writer(unicode(messages("LANGUAGE", langname)))
                __M_writer(u'</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if rss_link:
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 0, "20": 2, "21": 59, "22": 84, "23": 114, "24": 137, "25": 151, "26": 159, "32": 61, "41": 61, "42": 62, "43": 63, "44": 64, "45": 67, "46": 68, "47": 70, "48": 71, "49": 72, "50": 74, "51": 75, "52": 78, "53": 80, "54": 81, "55": 81, "56": 81, "57": 83, "58": 83, "59": 83, "65": 3, "88": 3, "89": 7, "90": 8, "91": 9, "92": 10, "93": 12, "94": 13, "95": 15, "96": 16, "97": 18, "98": 21, "99": 22, "100": 25, "101": 25, "102": 25, "103": 28, "104": 29, "105": 29, "106": 29, "107": 31, "108": 33, "109": 33, "110": 35, "111": 35, "112": 36, "113": 36, "114": 37, "115": 38, "116": 38, "117": 38, "118": 40, "119": 41, "120": 42, "121": 43, "122": 43, "123": 43, "124": 43, "125": 43, "126": 43, "127": 43, "128": 46, "129": 47, "130": 48, "131": 48, "132": 48, "133": 50, "134": 51, "135": 51, "136": 52, "137": 53, "138": 54, "139": 55, "140": 57, "141": 58, "142": 58, "148": 116, "158": 116, "159": 117, "160": 118, "161": 119, "162": 119, "163": 119, "164": 121, "165": 122, "166": 123, "167": 123, "168": 123, "169": 123, "170": 123, "171": 124, "172": 125, "173": 125, "174": 125, "175": 125, "176": 125, "177": 128, "178": 129, "179": 130, "180": 131, "181": 131, "182": 131, "183": 131, "184": 131, "185": 132, "186": 133, "187": 133, "188": 133, "189": 133, "190": 133, "196": 87, "206": 87, "207": 88, "208": 89, "209": 90, "210": 92, "211": 93, "212": 95, "213": 96, "214": 97, "215": 98, "216": 99, "217": 101, "218": 105, "219": 106, "220": 109, "221": 110, "222": 110, "223": 110, "224": 111, "225": 112, "226": 112, "227": 112, "233": 153, "241": 153, "242": 154, "243": 155, "244": 156, "245": 156, "246": 156, "247": 156, "248": 156, "249": 156, "250": 156, "256": 139, "265": 139, "266": 140, "267": 141, "268": 141, "269": 141, "270": 142, "271": 143, "272": 144, "273": 145, "274": 145, "275": 145, "276": 145, "277": 145, "278": 147, "279": 148, "280": 148, "281": 148, "287": 281}, "uri": "base_helper.tmpl", "filename": "themes/test/templates/base_helper.tmpl"}
__M_END_METADATA
"""
