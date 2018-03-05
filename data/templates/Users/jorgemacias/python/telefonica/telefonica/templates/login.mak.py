# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520293237.55354
_enable_loop = True
_template_filename = '/Users/jorgemacias/python/telefonica/telefonica/templates/login.mak'
_template_uri = '/Users/jorgemacias/python/telefonica/telefonica/templates/login.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        login_counter = context.get('login_counter', UNDEFINED)
        came_from = context.get('came_from', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset="utf-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<title>Lumino - Login</title>\n\n    <link href="')
        __M_writer(escape(tg.url('/css/bootstrap.min.css')))
        __M_writer(u'" rel="stylesheet">\n    <link href="')
        __M_writer(escape(tg.url('/css/datepicker3.css')))
        __M_writer(u'" rel="stylesheet" />\n    <link href="')
        __M_writer(escape(tg.url('/css/styles.css')))
        __M_writer(u'" rel="stylesheet">\n\n\t<!--[if lt IE 9]>\n\t<script src="')
        __M_writer(escape(tg.url('/js/html5/html5shiv.js')))
        __M_writer(u'"></script>\n\t<script src="')
        __M_writer(escape(tg.url('js/html5/respond.min.js')))
        __M_writer(u'"></script>\n\t<![endif]-->\n</head>\n<body>\n')

        flash=tg.flash_obj.render('flash', use_js=False)
          
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['flash'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if flash:
            __M_writer(u'      <div class="row">\n        <div class="col-md-8 col-md-offset-2">\n              ')
            __M_writer(flash )
            __M_writer(u'\n        </div>\n      </div>\n')
        else:
            __M_writer(u'    <br>\n')
        __M_writer(u'\t<div class="row">\n\t\t<div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-4 col-md-offset-4">\n\t\t\t<div class="login-panel panel panel-default">\n\t\t\t\t<div class="panel-heading">Log in</div>\n\t\t\t\t<div class="panel-body">\n\t\t\t\t\t<form role="form" action="')
        __M_writer(escape(tg.url('/login_handler', params=dict(came_from=came_from, __logins=login_counter))))
        __M_writer(u'" method="post" accept-charset="UTF-8">\n\t\t\t\t\t\t<fieldset>\n\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t<input class="form-control" placeholder="user" name="login" type="text" autofocus="">\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t<input class="form-control" placeholder="Password" name="password" type="password" value="">\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class="checkbox">\n\t\t\t\t\t\t\t\t<label>\n\t\t\t\t\t\t\t\t\t<input name="remember" type="checkbox" value="Remember Me">Remember Me\n\t\t\t\t\t\t\t\t</label>\n\t\t\t\t\t\t\t</div>\n                        <button type="submit" class="btn btn-primary">')
        __M_writer(escape(_('login')))
        __M_writer(u'</button>\n\n\t\t\t\t\t</form>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div><!-- /.col-->\n\t</div><!-- /.row -->\n\n\n    <script src="')
        __M_writer(escape(tg.url('/js/jquery-1.11.1.min.js')))
        __M_writer(u'"></script>\n\t<script src="')
        __M_writer(escape(tg.url('/js/bootstrap.min.js')))
        __M_writer(u'"></script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "27": 1, "28": 8, "29": 8, "30": 9, "31": 9, "32": 10, "33": 10, "34": 13, "35": 13, "36": 14, "37": 14, "38": 18, "44": 20, "45": 21, "46": 22, "47": 24, "48": 24, "49": 27, "50": 28, "51": 30, "52": 35, "53": 35, "54": 48, "55": 48, "56": 57, "57": 57, "58": 58, "59": 58, "65": 59}, "uri": "/Users/jorgemacias/python/telefonica/telefonica/templates/login.mak", "filename": "/Users/jorgemacias/python/telefonica/telefonica/templates/login.mak"}
__M_END_METADATA
"""
