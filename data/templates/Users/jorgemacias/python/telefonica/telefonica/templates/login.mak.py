# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520297252.251797
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
        login_counter = context.get('login_counter', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        str = context.get('str', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        came_from = context.get('came_from', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset="utf-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<title>Lumino - Login</title>\n\n    <link href="')
        __M_writer(escape(tg.url('/css/bootstrap.min.css')))
        __M_writer(u'" rel="stylesheet">\n    <link href="')
        __M_writer(escape(tg.url('/css/datepicker3.css')))
        __M_writer(u'" rel="stylesheet" />\n    <link href="')
        __M_writer(escape(tg.url('/css/styles.css')))
        __M_writer(u'" rel="stylesheet">\n    <script src="')
        __M_writer(escape(tg.url('/js/jquery-1.11.1.min.js')))
        __M_writer(u'"></script>\n    <script src="')
        __M_writer(escape(tg.url('/js/alert.js')))
        __M_writer(u'"></script>\n\t<!--[if lt IE 9]>\n\t<script src="')
        __M_writer(escape(tg.url('/js/html5/html5shiv.js')))
        __M_writer(u'"></script>\n\t<script src="')
        __M_writer(escape(tg.url('js/html5/respond.min.js')))
        __M_writer(u'"></script>\n\n\t<![endif]-->\n</head>\n<body>\n')

        flash=tg.flash_obj.render('flash', use_js=False)
          
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['flash'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if flash:
            __M_writer(u'      <div class="row">\n        <div class="col-md-8 col-md-offset-2">\n                <script>$.alert("')
            __M_writer(escape(str(tg.flash_obj.pop_payload()['message'])))
            __M_writer(u'" ,{autoclose:true,type:\'info\',title:false});</script>\n        </div>\n      </div>\n')
        else:
            __M_writer(u'    <br>\n')
        __M_writer(u'\t<div class="row">\n\t\t<div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-4 col-md-offset-4">\n\t\t\t<div class="login-panel panel panel-default">\n\t\t\t\t<div class="panel-heading">Log in</div>\n\t\t\t\t<div class="panel-body">\n\t\t\t\t\t<form role="form" action="')
        __M_writer(escape(tg.url('/login_handler', params=dict(came_from=came_from, __logins=login_counter))))
        __M_writer(u'" method="post" accept-charset="UTF-8">\n\t\t\t\t\t\t<fieldset>\n\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t<input class="form-control" placeholder="user" name="login" type="text" autofocus="">\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t<input class="form-control" placeholder="Password" name="password" type="password" value="">\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<div class="checkbox">\n\t\t\t\t\t\t\t\t<label>\n\t\t\t\t\t\t\t\t\t<input name="remember" type="checkbox" name="remember" value="2252000">Remember Me\n\t\t\t\t\t\t\t\t</label>\n\t\t\t\t\t\t\t</div>\n                        <button type="submit" class="btn btn-primary">')
        __M_writer(escape(_('login')))
        __M_writer(u'</button>\n\n\t\t\t\t\t</form>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div><!-- /.col-->\n\t</div><!-- /.row -->\n\n\n    <script src="')
        __M_writer(escape(tg.url('/js/jquery-1.11.1.min.js')))
        __M_writer(u'"></script>\n\t<script src="')
        __M_writer(escape(tg.url('/js/bootstrap.min.js')))
        __M_writer(u'"></script>\n<script src="')
        __M_writer(escape(tg.url('/js/alert.js')))
        __M_writer(u'"></script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 1, "29": 8, "30": 8, "31": 9, "32": 9, "33": 10, "34": 10, "35": 11, "36": 11, "37": 12, "38": 12, "39": 14, "40": 14, "41": 15, "42": 15, "43": 20, "49": 22, "50": 23, "51": 24, "52": 26, "53": 26, "54": 29, "55": 30, "56": 32, "57": 37, "58": 37, "59": 50, "60": 50, "61": 59, "62": 59, "63": 60, "64": 60, "65": 61, "66": 61, "72": 66}, "uri": "/Users/jorgemacias/python/telefonica/telefonica/templates/login.mak", "filename": "/Users/jorgemacias/python/telefonica/telefonica/templates/login.mak"}
__M_END_METADATA
"""
