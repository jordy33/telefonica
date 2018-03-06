<!DOCTYPE html>
<html>
<head>
    ${self.meta()}
    <link rel="icon" type="image/x-icon" href="${tg.url('/img/movistar.ico')}" />
    <title>${self.title()}</title>
    <link href="${tg.url('/css/bootstrap.min.css')}" rel="stylesheet">
    <link href="${tg.url('/css/font-awesome.min.css')}" rel="stylesheet" />
    <link href="${tg.url('/css/datepicker3.css')}" rel="stylesheet" />
    <link href="${tg.url('/css/styles.css')}" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css?family=Montserrat:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">
    <!-- jquery and alert -->
    <script src="${tg.url('/js/jquery-1.11.1.min.js')}"></script>
    <script src="${tg.url('/js/alert.js')}"></script>
	<!--[if lt IE 9]>
	<script src="${tg.url('/js/html5/html5shiv.js')}"></script>
	<script src="${tg.url('/js/html5/respond.min.js')}"></script>
	<![endif]-->
    <!-- jqgrid -->
    <script src="${tg.url('/js/jqgrid/jquery.jqgrid.min.js')}"></script>
    <script src="${tg.url('/js/jqgrid/i18n/grid.locale-es.js')}"></script>
    <!-- Font Size -->
    <link rel="stylesheet" href="${tg.url('/css/jqgrid/ui.jqgrid.css')}">
    <!-- Custom Theme Roller -->
    <!-- Important: Bootstrap must be first to avoid over raid jquery-ui  -->
    <script src="${tg.url('/js/bootstrap.min.js')}"></script>

    <script src="${tg.url('/js/jquery-ui.js')}"></script>
    <script src="${tg.url('/js/jquery-validation-1.17.0/dist/jquery.validate.js')}"></script>

    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/redmond/jquery-ui.css" type="text/css"/>
    <!-- end jqgrid -->
    <script src="${tg.url('/js/mqtt/mqttws31.js')}" type="text/javascript"></script>
    <!-- notifications grid -->
    <!-- moment for UTC to local dates -->
    <script src="${tg.url('/js/moment/moment.js')}"></script>


    <script src="js/lumino/chart.min.js"></script>
	<script src="js/lumino/chart-data.js"></script>
	<script src="js/lumino/easypiechart.js"></script>
	<script src="js/lumino/easypiechart-data.js"></script>
	<script src="js/lumino/bootstrap-datepicker.js"></script>
	<script src="js/lumino/custom.js"></script>

    <style type="text/css">
    html, body {
        margin: 0;
        padding: 0;
        font-size:100%;
    }
    </style>
    <!-- Global JavaScript -->
    <script type="text/javascript">
		window.onload = function () {
	    var chart1 = document.getElementById("line-chart").getContext("2d");
                    window.myLine = new Chart(chart1).Line(lineChartData, {
                    responsive: true,
                    scaleLineColor: "rgba(0,0,0,.2)",
                    scaleGridLineColor: "rgba(0,0,0,.05)",
                    scaleFontColor: "#c5c7cc"
                    });
        };
	</script>

    ${self.head_content()}
</head>

% if tg.auth_stack_enabled:
  % if not request.identity:
       <meta http-equiv="refresh" content="0; url=${tg.url('/login')}" />

  % else:
        <body class="${self.body_class()}">
          ${self.main_menu()}
          ${self.footer()}
        <!-- Insert nice scrool -->
          ${self.bottom_scripts()}
  % endif
% endif
</html>

<%def name="meta()">
    <meta charset="${response.charset}" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Bootstrap 3 App">
    <meta name="author" content="Jorge Macias">
    <meta name="keyword" content="Telefonica">
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
</%def>

<%def name="title()">  </%def>

<%def name="head_content()"></%def>

<%def name="body_class()"></%def>

<%def name="main_menu()">
  <!-- INSERT MAIN MENU -->
<nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse"><span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span></button>
				<a class="navbar-brand" href="#"><span>Telefonica</span> Movistar</a>
				<ul class="nav navbar-top-links navbar-right">
					<li class="dropdown"><a class="dropdown-toggle count-info" data-toggle="dropdown" href="#">
						<em class="fa fa-envelope"></em><span class="label label-danger">15</span>
					</a>
						<ul class="dropdown-menu dropdown-messages">
							<li>
								<div class="dropdown-messages-box"><a href="profile.html" class="pull-left">
									<img alt="image" class="img-circle" src="http://placehold.it/40/30a5ff/fff">
									</a>
									<div class="message-body"><small class="pull-right">3 mins ago</small>
										<a href="#"><strong>John Doe</strong> commented on <strong>your photo</strong>.</a>
									<br /><small class="text-muted">1:24 pm - 25/03/2015</small></div>
								</div>
							</li>
							<li class="divider"></li>
							<li>
								<div class="dropdown-messages-box"><a href="profile.html" class="pull-left">
									<img alt="image" class="img-circle" src="http://placehold.it/40/30a5ff/fff">
									</a>
									<div class="message-body"><small class="pull-right">1 hour ago</small>
										<a href="#">New message from <strong>Jane Doe</strong>.</a>
									<br /><small class="text-muted">12:27 pm - 25/03/2015</small></div>
								</div>
							</li>
							<li class="divider"></li>
							<li>
								<div class="all-button"><a href="#">
									<em class="fa fa-inbox"></em> <strong>All Messages</strong>
								</a></div>
							</li>
						</ul>
					</li>
					<li class="dropdown"><a class="dropdown-toggle count-info" data-toggle="dropdown" href="#">
						<em class="fa fa-bell"></em><span class="label label-info">5</span>
					</a>
						<ul class="dropdown-menu dropdown-alerts">
							<li><a href="#">
								<div><em class="fa fa-envelope"></em> 1 New Message
									<span class="pull-right text-muted small">3 mins ago</span></div>
							</a></li>
							<li class="divider"></li>
							<li><a href="#">
								<div><em class="fa fa-heart"></em> 12 New Likes
									<span class="pull-right text-muted small">4 mins ago</span></div>
							</a></li>
							<li class="divider"></li>
							<li><a href="#">
								<div><em class="fa fa-user"></em> 5 New Followers
									<span class="pull-right text-muted small">4 mins ago</span></div>
							</a></li>
						</ul>
					</li>
				</ul>
			</div>
		</div><!-- /.container-fluid -->
	</nav>
    <!-- End header -->

    <!-- Start Side Bar -->
    <div id="sidebar-collapse" class="col-sm-3 col-lg-2 sidebar">
		<div class="profile-sidebar">
			<div class="profile-userpic">
				<img src="${tg.url('/img/user.png')}" class="img-responsive" alt="">
			</div>
			<div class="profile-usertitle">
				<div class="profile-usertitle-name">${request.identity['repoze.who.userid']}</div>
				<div class="profile-usertitle-status"><span class="indicator label-success"></span>Online</div>
			</div>
			<div class="clear"></div>
		</div>
		<div class="divider"></div>
		<form role="search">
			<div class="form-group">
				<input type="text" class="form-control" placeholder="Search">
			</div>
		</form>
		<ul class="nav menu">
			<li class="active"><a href="index.html"><em class="fa fa-dashboard">&nbsp;</em> Dashboard</a></li>
			<li><a href="widgets.html"><em class="fa fa-calendar">&nbsp;</em> Widgets</a></li>
			<li><a href="charts.html"><em class="fa fa-bar-chart">&nbsp;</em> Charts</a></li>
			<li><a href="elements.html"><em class="fa fa-toggle-off">&nbsp;</em> UI Elements</a></li>
			<li><a href="panels.html"><em class="fa fa-clone">&nbsp;</em> Alerts &amp; Panels</a></li>
            <li><a href="jqgrid.html"><em class="fa fa-clone">&nbsp;</em> JqGrid</a></li>
            % if request.identity['repoze.who.userid']=='manager':
                <li><a href="test.html"><em class="fa fa-clone">&nbsp;</em> Test</a></li>
            % endif

			<li class="parent "><a data-toggle="collapse" href="#sub-item-1">

				<em class="fa fa-navicon">&nbsp;</em> Multilevel <span data-toggle="collapse" href="#sub-item-1" class="icon pull-right"><em class="fa fa-plus"></em></span>
				</a>
				<ul class="children collapse" id="sub-item-1">
					<li><a class="" href="#">
						<span class="fa fa-arrow-right">&nbsp;</span> Sub Item 1
					</a></li>
					<li><a class="" href="#">
						<span class="fa fa-arrow-right">&nbsp;</span> Sub Item 2
					</a></li>
					<li><a class="" href="#">
						<span class="fa fa-arrow-right">&nbsp;</span> Sub Item 3
					</a></li>
				</ul>
			</li>
			<li><a href="${tg.url('/logout_handler')}"><i class="icon_key_alt"></i>${_('Logout')}</a></li>
		</ul>
	</div>
  <br>
  <br>
  <br>
  <br>


    <!--/End Side Bar-->
  ${self.content_wrapper()}

</%def>


<%def name="content_wrapper()">
  <%
    flash=tg.flash_obj.render('flash', use_js=False)
  %>
  % if flash:
    <script>$.alert("${str(tg.flash_obj.pop_payload()['message'])}" ,{autoclose:false,type:'info',title:false});</script>
  % endif
  ${self.body()}
</%def>

<%def name="footer()">
   <!-- INSERT FOOTER -->
    <div class="text-right">
        <div class="credits">
              <p>Copyright &copy; Madd Systems ${h.current_year()}&nbsp;</p>
        </div>
    </div>
</%def>

<%def name="bottom_scripts()">
 <script>
 </script>
</%def>
