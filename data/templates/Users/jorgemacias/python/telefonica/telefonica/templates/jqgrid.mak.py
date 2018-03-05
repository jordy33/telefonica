# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520293674.137511
_enable_loop = True
_template_filename = '/Users/jorgemacias/python/telefonica/telefonica/templates/jqgrid.mak'
_template_uri = '/Users/jorgemacias/python/telefonica/telefonica/templates/jqgrid.mak'
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
        __M_writer(u'\n<!--main content start-->\n<section id="main-content">\n\n      <!-- page start-->\n\n    <div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">\n\t\t<div class="row">\n\t\t\t<ol class="breadcrumb">\n\t\t\t\t<li><a href="#">\n\t\t\t\t\t<em class="fa fa-home"></em>\n\t\t\t\t</a></li>\n\t\t\t\t<li class="active">Widgets</li>\n\t\t\t</ol>\n\t\t</div><!--/.row-->\n        <br>\n\t\t<div class="row">\n            <div style="margin-left:20px">\n            <table id="jqGrid"></table>\n            <div id="jqGridPager"></div>\n            </div>\n\t\t</div><!--/.row-->\n\n\t\t\n\n      <!-- page end-->\n</div>\n  </section>\n</section>\n\n')
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
        __M_writer(u'\n\n   <style type="text/css">\n   </style>\n\n   <script type="text/javascript">\n        $(document).ready(function () {\n\n            $("#jqGrid").jqGrid({\n                url: \'http://trirand.com/blog/phpjqgrid/examples/jsonp/getjsonp.php?callback=?&qwery=longorders\',\n                mtype: "GET",\n\t\t\t\tstyleUI : \'Bootstrap\',\n                datatype: "jsonp",\n                colModel: [\n                    { label: \'OrderID\', name: \'OrderID\', key: true, width: 75 },\n                    { label: \'Customer ID\', name: \'CustomerID\', width: 150 },\n                    { label: \'Order Date\', name: \'OrderDate\', width: 150 },\n                    { label: \'Freight\', name: \'Freight\', width: 150 },\n                    { label:\'Ship Name\', name: \'ShipName\', width: 150 }\n                ],\n\t\t\t\tviewrecords: true,\n                height: 250,\n                rowNum: 20,\n                pager: "#jqGridPager"\n            });\n        });\n\n   </script>\n\n')
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
{"source_encoding": "utf-8", "line_map": {"33": 1, "34": 4, "35": 34, "36": 65, "72": 66, "42": 64, "66": 2, "46": 64, "52": 5, "56": 5, "28": 0, "62": 2}, "uri": "/Users/jorgemacias/python/telefonica/telefonica/templates/jqgrid.mak", "filename": "/Users/jorgemacias/python/telefonica/telefonica/templates/jqgrid.mak"}
__M_END_METADATA
"""
