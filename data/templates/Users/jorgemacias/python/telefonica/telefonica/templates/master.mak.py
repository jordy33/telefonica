# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520296417.267831
_enable_loop = True
_template_filename = u'/Users/jorgemacias/python/telefonica/telefonica/templates/master.mak'
_template_uri = u'/Users/jorgemacias/python/telefonica/telefonica/templates/master.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['footer', 'title', 'body_class', 'head_content', 'bottom_scripts', 'meta', 'main_menu', 'content_wrapper']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n<head>\n    ')
        __M_writer(escape(self.meta()))
        __M_writer(u'\n    <link rel="icon" type="image/x-icon" href="')
        __M_writer(escape(tg.url('/img/movistar.ico')))
        __M_writer(u'" />\n    <title>')
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n    <link href="')
        __M_writer(escape(tg.url('/css/bootstrap.min.css')))
        __M_writer(u'" rel="stylesheet">\n    <link href="')
        __M_writer(escape(tg.url('/css/font-awesome.min.css')))
        __M_writer(u'" rel="stylesheet" />\n    <link href="')
        __M_writer(escape(tg.url('/css/datepicker3.css')))
        __M_writer(u'" rel="stylesheet" />\n    <link href="')
        __M_writer(escape(tg.url('/css/styles.css')))
        __M_writer(u'" rel="stylesheet">\n\t<link href="https://fonts.googleapis.com/css?family=Montserrat:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">\n    <!-- jquery and alert -->\n    <script src="')
        __M_writer(escape(tg.url('/js/jquery-1.11.1.min.js')))
        __M_writer(u'"></script>\n    <script src="')
        __M_writer(escape(tg.url('/js/alert.js')))
        __M_writer(u'"></script>\n\n    <!-- jqgrid -->\n    <script src="')
        __M_writer(escape(tg.url('/js/jqgrid/jquery.jqgrid.min.js')))
        __M_writer(u'"></script>\n    <script src="')
        __M_writer(escape(tg.url('/js/jqgrid/i18n/grid.locale-es.js')))
        __M_writer(u'"></script>\n    <!-- Font Size -->\n    <link rel="stylesheet" href="')
        __M_writer(escape(tg.url('/css/jqgrid/ui.jqgrid.css')))
        __M_writer(u'">\n    <!-- Custom Theme Roller -->\n    <!-- Important: Bootstrap must be first to avoid over raid jquery-ui  -->\n    <script src="')
        __M_writer(escape(tg.url('/js/bootstrap.min.js')))
        __M_writer(u'"></script>\n\n    <script src="')
        __M_writer(escape(tg.url('/js/jquery-ui.js')))
        __M_writer(u'"></script>\n    <script src="')
        __M_writer(escape(tg.url('/js/jquery-validation-1.17.0/dist/jquery.validate.js')))
        __M_writer(u'"></script>\n\n    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>\n    <!-- end jqgrid -->\n    <script src="')
        __M_writer(escape(tg.url('/js/mqtt/mqttws31.js')))
        __M_writer(u'" type="text/javascript"></script>\n    <!-- notifications grid -->\n    <!-- moment for UTC to local dates -->\n    <script src="')
        __M_writer(escape(tg.url('/js/moment/moment.js')))
        __M_writer(u'"></script>\n\n\n    <script src="js/lumino/chart.min.js"></script>\n\t<script src="js/lumino/chart-data.js"></script>\n\t<script src="js/lumino/easypiechart.js"></script>\n\t<script src="js/lumino/easypiechart-data.js"></script>\n\t<script src="js/lumino/bootstrap-datepicker.js"></script>\n\t<script src="js/lumino/custom.js"></script>\n\n    <style type="text/css">\n    html, body {\n        margin: 0;\n        padding: 0;\n        font-size:90%;\n    }\n    </style>\n    <!-- Global JavaScript -->\n    <script type="text/javascript">\n\t\twindow.onload = function () {\n\t    var chart1 = document.getElementById("line-chart").getContext("2d");\n                    window.myLine = new Chart(chart1).Line(lineChartData, {\n                    responsive: true,\n                    scaleLineColor: "rgba(0,0,0,.2)",\n                    scaleGridLineColor: "rgba(0,0,0,.05)",\n                    scaleFontColor: "#c5c7cc"\n                    });\n        };\n\t</script>\n\n    ')
        __M_writer(escape(self.head_content()))
        __M_writer(u'\n</head>\n\n')
        if tg.auth_stack_enabled:
            if not request.identity:
                __M_writer(u'       <meta http-equiv="refresh" content="0; url=')
                __M_writer(escape(tg.url('/login')))
                __M_writer(u'" />\n\n')
            else:
                __M_writer(u'        <body class="')
                __M_writer(escape(self.body_class()))
                __M_writer(u'">\n          ')
                __M_writer(escape(self.main_menu()))
                __M_writer(u'\n          ')
                __M_writer(escape(self.footer()))
                __M_writer(u'\n        <!-- Insert nice scrool -->\n          ')
                __M_writer(escape(self.bottom_scripts()))
                __M_writer(u'\n')
        __M_writer(u'</html>\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n   <!-- INSERT FOOTER -->\n    <div class="col-sm-12">\n        <p class="back-link">Copyright &copy; Madd Systems ')
        __M_writer(escape(h.current_year()))
        __M_writer(u'&nbsp;</p>\n\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottom_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n <script>\n </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        response = context.get('response', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <meta charset="')
        __M_writer(escape(response.charset))
        __M_writer(u'" />\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="description" content="Bootstrap 3 App">\n    <meta name="author" content="Jorge Macias">\n    <meta name="keyword" content="Telefonica">\n    <meta name="viewport" content="initial-scale=1.0">\n    <meta charset="utf-8">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  <!-- INSERT MAIN MENU -->\n<nav class="navbar navbar-custom navbar-fixed-top" role="navigation">\n\t\t<div class="container-fluid">\n\t\t\t<div class="navbar-header">\n\t\t\t\t<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse"><span class="sr-only">Toggle navigation</span>\n\t\t\t\t\t<span class="icon-bar"></span>\n\t\t\t\t\t<span class="icon-bar"></span>\n\t\t\t\t\t<span class="icon-bar"></span></button>\n\t\t\t\t<a class="navbar-brand" href="#"><span>Telefonica</span> Movistar</a>\n\t\t\t\t<ul class="nav navbar-top-links navbar-right">\n\t\t\t\t\t<li class="dropdown"><a class="dropdown-toggle count-info" data-toggle="dropdown" href="#">\n\t\t\t\t\t\t<em class="fa fa-envelope"></em><span class="label label-danger">15</span>\n\t\t\t\t\t</a>\n\t\t\t\t\t\t<ul class="dropdown-menu dropdown-messages">\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<div class="dropdown-messages-box"><a href="profile.html" class="pull-left">\n\t\t\t\t\t\t\t\t\t<img alt="image" class="img-circle" src="http://placehold.it/40/30a5ff/fff">\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<div class="message-body"><small class="pull-right">3 mins ago</small>\n\t\t\t\t\t\t\t\t\t\t<a href="#"><strong>John Doe</strong> commented on <strong>your photo</strong>.</a>\n\t\t\t\t\t\t\t\t\t<br /><small class="text-muted">1:24 pm - 25/03/2015</small></div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<div class="dropdown-messages-box"><a href="profile.html" class="pull-left">\n\t\t\t\t\t\t\t\t\t<img alt="image" class="img-circle" src="http://placehold.it/40/30a5ff/fff">\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<div class="message-body"><small class="pull-right">1 hour ago</small>\n\t\t\t\t\t\t\t\t\t\t<a href="#">New message from <strong>Jane Doe</strong>.</a>\n\t\t\t\t\t\t\t\t\t<br /><small class="text-muted">12:27 pm - 25/03/2015</small></div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<div class="all-button"><a href="#">\n\t\t\t\t\t\t\t\t\t<em class="fa fa-inbox"></em> <strong>All Messages</strong>\n\t\t\t\t\t\t\t\t</a></div>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</li>\n\t\t\t\t\t<li class="dropdown"><a class="dropdown-toggle count-info" data-toggle="dropdown" href="#">\n\t\t\t\t\t\t<em class="fa fa-bell"></em><span class="label label-info">5</span>\n\t\t\t\t\t</a>\n\t\t\t\t\t\t<ul class="dropdown-menu dropdown-alerts">\n\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t<div><em class="fa fa-envelope"></em> 1 New Message\n\t\t\t\t\t\t\t\t\t<span class="pull-right text-muted small">3 mins ago</span></div>\n\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t<div><em class="fa fa-heart"></em> 12 New Likes\n\t\t\t\t\t\t\t\t\t<span class="pull-right text-muted small">4 mins ago</span></div>\n\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t\t<li class="divider"></li>\n\t\t\t\t\t\t\t<li><a href="#">\n\t\t\t\t\t\t\t\t<div><em class="fa fa-user"></em> 5 New Followers\n\t\t\t\t\t\t\t\t\t<span class="pull-right text-muted small">4 mins ago</span></div>\n\t\t\t\t\t\t\t</a></li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</li>\n\t\t\t\t</ul>\n\t\t\t</div>\n\t\t</div><!-- /.container-fluid -->\n\t</nav>\n    <!-- End header -->\n\n    <!-- Start Side Bar -->\n    <div id="sidebar-collapse" class="col-sm-3 col-lg-2 sidebar">\n\t\t<div class="profile-sidebar">\n\t\t\t<div class="profile-userpic">\n\t\t\t\t<img src="')
        __M_writer(escape(tg.url('/img/user.png')))
        __M_writer(u'" class="img-responsive" alt="">\n\t\t\t</div>\n\t\t\t<div class="profile-usertitle">\n\t\t\t\t<div class="profile-usertitle-name">')
        __M_writer(escape(request.identity['repoze.who.userid']))
        __M_writer(u'</div>\n\t\t\t\t<div class="profile-usertitle-status"><span class="indicator label-success"></span>Online</div>\n\t\t\t</div>\n\t\t\t<div class="clear"></div>\n\t\t</div>\n\t\t<div class="divider"></div>\n\t\t<form role="search">\n\t\t\t<div class="form-group">\n\t\t\t\t<input type="text" class="form-control" placeholder="Search">\n\t\t\t</div>\n\t\t</form>\n\t\t<ul class="nav menu">\n\t\t\t<li class="active"><a href="index.html"><em class="fa fa-dashboard">&nbsp;</em> Dashboard</a></li>\n\t\t\t<li><a href="widgets.html"><em class="fa fa-calendar">&nbsp;</em> Widgets</a></li>\n\t\t\t<li><a href="charts.html"><em class="fa fa-bar-chart">&nbsp;</em> Charts</a></li>\n\t\t\t<li><a href="elements.html"><em class="fa fa-toggle-off">&nbsp;</em> UI Elements</a></li>\n\t\t\t<li><a href="panels.html"><em class="fa fa-clone">&nbsp;</em> Alerts &amp; Panels</a></li>\n            <li><a href="jqgrid.html"><em class="fa fa-clone">&nbsp;</em> JqGrid</a></li>\n')
        if request.identity['repoze.who.userid']=='manager':
            __M_writer(u'                <li><a href="test.html"><em class="fa fa-clone">&nbsp;</em> Test</a></li>\n')
        __M_writer(u'\n\t\t\t<li class="parent "><a data-toggle="collapse" href="#sub-item-1">\n\n\t\t\t\t<em class="fa fa-navicon">&nbsp;</em> Multilevel <span data-toggle="collapse" href="#sub-item-1" class="icon pull-right"><em class="fa fa-plus"></em></span>\n\t\t\t\t</a>\n\t\t\t\t<ul class="children collapse" id="sub-item-1">\n\t\t\t\t\t<li><a class="" href="#">\n\t\t\t\t\t\t<span class="fa fa-arrow-right">&nbsp;</span> Sub Item 1\n\t\t\t\t\t</a></li>\n\t\t\t\t\t<li><a class="" href="#">\n\t\t\t\t\t\t<span class="fa fa-arrow-right">&nbsp;</span> Sub Item 2\n\t\t\t\t\t</a></li>\n\t\t\t\t\t<li><a class="" href="#">\n\t\t\t\t\t\t<span class="fa fa-arrow-right">&nbsp;</span> Sub Item 3\n\t\t\t\t\t</a></li>\n\t\t\t\t</ul>\n\t\t\t</li>\n\t\t\t<li><a href="')
        __M_writer(escape(tg.url('/logout_handler')))
        __M_writer(u'"><i class="icon_key_alt"></i>')
        __M_writer(escape(_('Logout')))
        __M_writer(u'</a></li>\n\t\t</ul>\n\t</div>\n  <br>\n  <br>\n  <br>\n  <br>\n\n\n    <!--/End Side Bar-->\n  ')
        __M_writer(escape(self.content_wrapper()))
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  ')

        flash=tg.flash_obj.render('flash', use_js=False)
          
        
        __M_writer(u'\n')
        if flash:
            __M_writer(u'    <script>$.alert("')
            __M_writer(escape(str(tg.flash_obj.pop_payload()['message'])))
            __M_writer(u'" ,{autoclose:false,type:\'info\',title:false});</script>\n')
        __M_writer(u'  ')
        __M_writer(escape(self.body()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "25": 1, "26": 4, "27": 4, "28": 5, "29": 5, "30": 6, "31": 6, "32": 7, "33": 7, "34": 8, "35": 8, "36": 9, "37": 9, "38": 10, "39": 10, "40": 13, "41": 13, "42": 14, "43": 14, "44": 17, "45": 17, "46": 18, "47": 18, "48": 20, "49": 20, "50": 23, "51": 23, "52": 25, "53": 25, "54": 26, "55": 26, "56": 30, "57": 30, "58": 33, "59": 33, "60": 63, "61": 63, "62": 66, "63": 67, "64": 68, "65": 68, "66": 68, "67": 70, "68": 71, "69": 71, "70": 71, "71": 72, "72": 72, "73": 73, "74": 73, "75": 75, "76": 75, "77": 78, "78": 88, "79": 90, "80": 92, "81": 94, "82": 221, "83": 232, "84": 240, "85": 245, "91": 234, "96": 234, "97": 237, "98": 237, "104": 90, "108": 90, "114": 94, "123": 92, "132": 242, "136": 242, "142": 80, "147": 80, "148": 81, "149": 81, "155": 96, "163": 96, "164": 168, "165": 168, "166": 171, "167": 171, "168": 189, "169": 190, "170": 192, "171": 209, "172": 209, "173": 209, "174": 209, "175": 219, "176": 219, "182": 224, "189": 224, "190": 225, "194": 227, "195": 228, "196": 229, "197": 229, "198": 229, "199": 231, "200": 231, "201": 231, "207": 201}, "uri": "/Users/jorgemacias/python/telefonica/telefonica/templates/master.mak", "filename": "/Users/jorgemacias/python/telefonica/telefonica/templates/master.mak"}
__M_END_METADATA
"""
