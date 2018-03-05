# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520293092.980538
_enable_loop = True
_template_filename = '/Users/jorgemacias/python/telefonica/telefonica/templates/elements.mak'
_template_uri = '/Users/jorgemacias/python/telefonica/telefonica/templates/elements.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['bottom_scripts', 'head_content', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n<!--main content start-->\n<section id="main-content">\n\n      <!-- page start-->\n    <div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">\n\t\t<div class="row">\n\t\t\t<ol class="breadcrumb">\n\t\t\t\t<li><a href="#">\n\t\t\t\t\t<em class="fa fa-home"></em>\n\t\t\t\t</a></li>\n\t\t\t\t<li class="active">Forms</li>\n\t\t\t</ol>\n\t\t</div><!--/.row-->\n\n\t\t<div class="row">\n\t\t\t<div class="col-lg-12">\n\t\t\t\t<h1 class="page-header">UI Elements</h1>\n\t\t\t</div>\n\t\t</div><!--/.row-->\n\n\n\t\t<div class="row">\n\t\t\t<div class="col-lg-12">\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-heading">Buttons</div>\n\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<div class="col-md-12">\n\t\t\t\t\t\t\t<h5>Small</h5>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-sm btn-primary">Primary</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-sm btn-default">Default</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-sm btn-success">Success</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-sm btn-info">Info</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-sm btn-warning">Warning</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-sm btn-danger">Danger</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-sm btn-link">Link</button>\n\t\t\t\t\t\t\t<br />\n\t\t\t\t\t\t\t<br />\n\t\t\t\t\t\t\t<h5>Medium</h5>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-md btn-primary">Primary</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-md btn-default">Default</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-md btn-success">Success</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-md btn-info">Info</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-md btn-warning">Warning</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-md btn-danger">Danger</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-md btn-link">Link</button>\n\t\t\t\t\t\t\t<br />\n\t\t\t\t\t\t\t<br />\n\t\t\t\t\t\t\t<h5>Large</h5>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-lg btn-primary">Primary</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-lg btn-default">Default</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-lg btn-success">Success</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-lg btn-info">Info</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-lg btn-warning">Warning</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-lg btn-danger">Danger</button>\n\t\t\t\t\t\t\t<button type="button" class="btn btn-lg btn-link">Link</button>\n\t\t\t\t\t\t\t<br />\n\t\t\t\t\t\t\t<br />\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div><!-- /.panel-->\n\n\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-heading">Forms</div>\n\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<div class="col-md-6">\n\t\t\t\t\t\t\t<form role="form">\n\t\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t\t<label>Text Input</label>\n\t\t\t\t\t\t\t\t\t<input class="form-control" placeholder="Placeholder">\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t\t<label>Password</label>\n\t\t\t\t\t\t\t\t\t<input type="password" class="form-control">\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class="form-group checkbox">\n\t\t\t\t\t\t\t\t\t<label>\n\t\t\t\t\t\t\t\t\t\t<input type="checkbox">Remember me\n\t\t\t\t\t\t\t\t\t</label>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t\t<label>File input</label>\n\t\t\t\t\t\t\t\t\t<input type="file">\n\t\t\t\t\t\t\t\t\t<p class="help-block">Example block-level help text here.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t\t<label>Text area</label>\n\t\t\t\t\t\t\t\t\t<textarea class="form-control" rows="3"></textarea>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<label>Validation</label>\n\t\t\t\t\t\t\t\t<div class="form-group has-success">\n\t\t\t\t\t\t\t\t\t<input class="form-control" placeholder="Success">\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class="form-group has-warning">\n\t\t\t\t\t\t\t\t\t<input class="form-control" placeholder="Warning">\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class="form-group has-error">\n\t\t\t\t\t\t\t\t\t<input class="form-control" placeholder="Error">\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class="col-md-6">\n\t\t\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t\t\t<label>Checkboxes</label>\n\t\t\t\t\t\t\t\t\t\t<div class="checkbox">\n\t\t\t\t\t\t\t\t\t\t\t<label>\n\t\t\t\t\t\t\t\t\t\t\t\t<input type="checkbox" value="">Checkbox 1\n\t\t\t\t\t\t\t\t\t\t\t</label>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="checkbox">\n\t\t\t\t\t\t\t\t\t\t\t<label>\n\t\t\t\t\t\t\t\t\t\t\t\t<input type="checkbox" value="">Checkbox 2\n\t\t\t\t\t\t\t\t\t\t\t</label>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="checkbox">\n\t\t\t\t\t\t\t\t\t\t\t<label>\n\t\t\t\t\t\t\t\t\t\t\t\t<input type="checkbox" value="">Checkbox 3\n\t\t\t\t\t\t\t\t\t\t\t</label>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="checkbox">\n\t\t\t\t\t\t\t\t\t\t\t<label>\n\t\t\t\t\t\t\t\t\t\t\t\t<input type="checkbox" value="">Checkbox 4\n\t\t\t\t\t\t\t\t\t\t\t</label>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t\t\t<label>Radio Buttons</label>\n\t\t\t\t\t\t\t\t\t\t<div class="radio">\n\t\t\t\t\t\t\t\t\t\t\t<label>\n\t\t\t\t\t\t\t\t\t\t\t\t<input type="radio" name="optionsRadios" id="optionsRadios1" value="option1" checked>Radio Button 1\n\t\t\t\t\t\t\t\t\t\t\t</label>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="radio">\n\t\t\t\t\t\t\t\t\t\t\t<label>\n\t\t\t\t\t\t\t\t\t\t\t\t<input type="radio" name="optionsRadios" id="optionsRadios2" value="option2">Radio Button 2\n\t\t\t\t\t\t\t\t\t\t\t</label>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="radio">\n\t\t\t\t\t\t\t\t\t\t\t<label>\n\t\t\t\t\t\t\t\t\t\t\t\t<input type="radio" name="optionsRadios" id="optionsRadios3" value="option3">Radio Button 3\n\t\t\t\t\t\t\t\t\t\t\t</label>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="radio">\n\t\t\t\t\t\t\t\t\t\t\t<label>\n\t\t\t\t\t\t\t\t\t\t\t\t<input type="radio" name="optionsRadios" id="optionsRadios3" value="option3">Radio Button 4\n\t\t\t\t\t\t\t\t\t\t\t</label>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t\t\t<label>Selects</label>\n\t\t\t\t\t\t\t\t\t\t<select class="form-control">\n\t\t\t\t\t\t\t\t\t\t\t<option>Option 1</option>\n\t\t\t\t\t\t\t\t\t\t\t<option>Option 2</option>\n\t\t\t\t\t\t\t\t\t\t\t<option>Option 3</option>\n\t\t\t\t\t\t\t\t\t\t\t<option>Option 4</option>\n\t\t\t\t\t\t\t\t\t\t</select>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t\t\t<label>Multiple Selects</label>\n\t\t\t\t\t\t\t\t\t\t<select multiple class="form-control">\n\t\t\t\t\t\t\t\t\t\t\t<option>Option 1</option>\n\t\t\t\t\t\t\t\t\t\t\t<option>Option 2</option>\n\t\t\t\t\t\t\t\t\t\t\t<option>Option 3</option>\n\t\t\t\t\t\t\t\t\t\t\t<option>Option 4</option>\n\t\t\t\t\t\t\t\t\t\t</select>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t<button type="submit" class="btn btn-primary">Submit Button</button>\n\t\t\t\t\t\t\t\t\t<button type="reset" class="btn btn-default">Reset Button</button>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</form>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div><!-- /.panel-->\n\t\t\t</div><!-- /.col-->\n\t\t\t<div class="col-sm-12">\n\t\t\t\t<p class="back-link">Lumino Theme by <a href="https://www.medialoot.com">Medialoot</a></p>\n\t\t\t</div>\n\t\t</div><!-- /.row -->\n\t</div><!--/.main-->\n      <!-- page end-->\n</div>\n  </section>\n</section>\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottom_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n\n   <style type="text/css">\n   </style>\n\n   <script type="text/javascript">\n   </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n  Welcome to Mercury\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 1, "34": 4, "35": 13, "36": 198, "72": 66, "42": 197, "66": 2, "46": 197, "52": 5, "56": 5, "28": 0, "62": 2}, "uri": "/Users/jorgemacias/python/telefonica/telefonica/templates/elements.mak", "filename": "/Users/jorgemacias/python/telefonica/telefonica/templates/elements.mak"}
__M_END_METADATA
"""
