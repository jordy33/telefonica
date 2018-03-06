# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520295740.068263
_enable_loop = True
_template_filename = '/Users/jorgemacias/python/telefonica/telefonica/templates/charts.mak'
_template_uri = '/Users/jorgemacias/python/telefonica/telefonica/templates/charts.mak'
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
        __M_writer(u'\n<!--main content start-->\n<section id="main-content">\n\n      <!-- page start-->\n    <div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">\n\t\t<div class="row">\n\t\t\t<ol class="breadcrumb">\n\t\t\t\t<li><a href="#">\n\t\t\t\t\t<em class="fa fa-home"></em>\n\t\t\t\t</a></li>\n\t\t\t\t<li class="active">Charts</li>\n\t\t\t</ol>\n\t\t</div><!--/.row-->\n\n\t\t<div class="row">\n\t\t\t<div class="col-lg-12">\n\t\t\t\t<h1 class="page-header">Charts</h1>\n\t\t\t</div>\n\t\t</div><!--/.row-->\n\n\t\t<div class="row">\n\t\t\t<div class="col-xs-6 col-md-3">\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-body easypiechart-panel">\n\t\t\t\t\t\t<div class="easypiechart" id="easypiechart-teal" data-percent="56" ><span class="percent">56%</span></div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="col-xs-6 col-md-3">\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-body easypiechart-panel">\n\t\t\t\t\t\t<div class="easypiechart" id="easypiechart-blue" data-percent="92" ><span class="percent">92%</span></div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="col-xs-6 col-md-3">\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-body easypiechart-panel">\n\t\t\t\t\t\t<div class="easypiechart" id="easypiechart-orange" data-percent="65" ><span class="percent">65%</span></div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="col-xs-6 col-md-3">\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-body easypiechart-panel">\n\t\t\t\t\t\t<div class="easypiechart" id="easypiechart-red" data-percent="27" ><span class="percent">27%</span></div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div><!--/.row-->\n\n\t\t<div class="row">\n\t\t\t<div class="col-lg-12">\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\tLine Chart\n\t\t\t\t\t\t<ul class="pull-right panel-settings panel-button-tab-right">\n\t\t\t\t\t\t\t<li class="dropdown"><a class="pull-right dropdown-toggle" data-toggle="dropdown" href="#">\n\t\t\t\t\t\t\t\t<em class="fa fa-cogs"></em>\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t<ul class="dropdown-menu dropdown-menu-right">\n\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t\t<ul class="dropdown-settings">\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 1\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 2\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 3\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t<span class="pull-right clickable panel-toggle panel-button-tab-left"><em class="fa fa-toggle-up"></em></span></div>\n\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<div class="canvas-wrapper">\n\t\t\t\t\t\t\t<canvas class="main-chart" id="line-chart" height="200" width="600"></canvas>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div><!--/.row-->\n\n\t\t<div class="row">\n\t\t\t<div class="col-lg-12">\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\tBar Chart\n\t\t\t\t\t\t<ul class="pull-right panel-settings panel-button-tab-right">\n\t\t\t\t\t\t\t<li class="dropdown"><a class="pull-right dropdown-toggle" data-toggle="dropdown" href="#">\n\t\t\t\t\t\t\t\t<em class="fa fa-cogs"></em>\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t<ul class="dropdown-menu dropdown-menu-right">\n\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t\t<ul class="dropdown-settings">\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 1\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 2\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 3\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t<span class="pull-right clickable panel-toggle panel-button-tab-left"><em class="fa fa-toggle-up"></em></span></div>\n\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<div class="canvas-wrapper">\n\t\t\t\t\t\t\t<canvas class="main-chart" id="bar-chart" height="200" width="600"></canvas>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div><!--/.row-->\n\n\t\t<div class="row">\n\t\t\t<div class="col-md-6">\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\tPie Chart\n\t\t\t\t\t\t<ul class="pull-right panel-settings panel-button-tab-right">\n\t\t\t\t\t\t\t<li class="dropdown"><a class="pull-right dropdown-toggle" data-toggle="dropdown" href="#">\n\t\t\t\t\t\t\t\t<em class="fa fa-cogs"></em>\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t<ul class="dropdown-menu dropdown-menu-right">\n\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t\t<ul class="dropdown-settings">\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 1\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 2\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 3\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t<span class="pull-right clickable panel-toggle panel-button-tab-left"><em class="fa fa-toggle-up"></em></span></div>\n\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<div class="canvas-wrapper">\n\t\t\t\t\t\t\t<canvas class="chart" id="pie-chart" ></canvas>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="col-md-6">\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\tDoughnut Chart\n\t\t\t\t\t\t<ul class="pull-right panel-settings panel-button-tab-right">\n\t\t\t\t\t\t\t<li class="dropdown"><a class="pull-right dropdown-toggle" data-toggle="dropdown" href="#">\n\t\t\t\t\t\t\t\t<em class="fa fa-cogs"></em>\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t<ul class="dropdown-menu dropdown-menu-right">\n\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t\t<ul class="dropdown-settings">\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 1\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 2\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 3\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t<span class="pull-right clickable panel-toggle panel-button-tab-left"><em class="fa fa-toggle-up"></em></span></div>\n\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<div class="canvas-wrapper">\n\t\t\t\t\t\t\t<canvas class="chart" id="doughnut-chart" ></canvas>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div><!--/.row-->\n\n\t\t<div class="row">\n\t\t\t<div class="col-md-6">\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\tRadar Chart\n\t\t\t\t\t\t<ul class="pull-right panel-settings panel-button-tab-right">\n\t\t\t\t\t\t\t<li class="dropdown"><a class="pull-right dropdown-toggle" data-toggle="dropdown" href="#">\n\t\t\t\t\t\t\t\t<em class="fa fa-cogs"></em>\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t<ul class="dropdown-menu dropdown-menu-right">\n\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t\t<ul class="dropdown-settings">\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 1\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 2\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 3\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t<span class="pull-right clickable panel-toggle panel-button-tab-left"><em class="fa fa-toggle-up"></em></span></div>\n\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<div class="canvas-wrapper">\n\t\t\t\t\t\t\t<canvas class="chart" id="radar-chart" ></canvas>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="col-md-6">\n\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\tPolar Area Chart\n\t\t\t\t\t\t<ul class="pull-right panel-settings panel-button-tab-right">\n\t\t\t\t\t\t\t<li class="dropdown"><a class="pull-right dropdown-toggle" data-toggle="dropdown" href="#">\n\t\t\t\t\t\t\t\t<em class="fa fa-cogs"></em>\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t<ul class="dropdown-menu dropdown-menu-right">\n\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t\t<ul class="dropdown-settings">\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 1\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 2\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t\t\t\t\t<em class="fa fa-cog"></em> Settings 3\n\t\t\t\t\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t<span class="pull-right clickable panel-toggle panel-button-tab-left"><em class="fa fa-toggle-up"></em></span></div>\n\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t<div class="canvas-wrapper">\n\t\t\t\t\t\t\t<canvas class="chart" id="polar-area-chart" ></canvas>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="col-sm-12">\n\t\t\t\t<p class="back-link">Lumino Theme by <a href="https://www.medialoot.com">Medialoot</a></p>\n\t\t\t</div>\n\t\t</div><!--/.row-->\n\t</div>\t<!--/.\n      <!-- page end-->\n</div>\n  </section>\n</section>\n\n')
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
        __M_writer(u'\n  Welcome to Telefonica\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 1, "34": 4, "35": 13, "36": 296, "72": 66, "42": 295, "66": 2, "46": 295, "52": 5, "56": 5, "28": 0, "62": 2}, "uri": "/Users/jorgemacias/python/telefonica/telefonica/templates/charts.mak", "filename": "/Users/jorgemacias/python/telefonica/telefonica/templates/charts.mak"}
__M_END_METADATA
"""
