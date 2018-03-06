<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Telefonica</title>

    <link href="${tg.url('/css/bootstrap.min.css')}" rel="stylesheet">
    <link href="${tg.url('/css/datepicker3.css')}" rel="stylesheet" />
    <link href="${tg.url('/css/styles.css')}" rel="stylesheet">
    <script src="${tg.url('/js/jquery-1.11.1.min.js')}"></script>
    <script src="${tg.url('/js/alert.js')}"></script>
	<!--[if lt IE 9]>
	<script src="${tg.url('/js/html5/html5shiv.js')}"></script>
	<script src="${tg.url('/js/html5/respond.min.js')}"></script>
	<![endif]-->
</head>
<body>
<%
    flash=tg.flash_obj.render('flash', use_js=False)
  %>
  % if flash:
      <div class="row">
        <div class="col-md-8 col-md-offset-2">
                <script>$.alert("${str(tg.flash_obj.pop_payload()['message'])}" ,{autoclose:true,type:'info',title:false});</script>
        </div>
      </div>
  % else:
    <br>
  % endif
	<div class="row">
		<div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-4 col-md-offset-4">
			<div class="login-panel panel panel-default">
				<div class="panel-heading">Log in</div>
				<div class="panel-body">
					<form role="form" action="${tg.url('/login_handler', params=dict(came_from=came_from, __logins=login_counter))}" method="post" accept-charset="UTF-8">
						<fieldset>
							<div class="form-group">
								<input class="form-control" placeholder="user" name="login" type="text" autofocus="">
							</div>
							<div class="form-group">
								<input class="form-control" placeholder="Password" name="password" type="password" value="">
							</div>
							<div class="checkbox">
								<label>
									<input name="remember" type="checkbox" name="remember" value="2252000">Remember Me
								</label>
							</div>
                        <button type="submit" class="btn btn-primary">${_('login')}</button>

					</form>
				</div>
			</div>
		</div><!-- /.col-->
	</div><!-- /.row -->
    <script src="${tg.url('/js/jquery-1.11.1.min.js')}"></script>
	<script src="${tg.url('/js/bootstrap.min.js')}"></script>
<script src="${tg.url('/js/alert.js')}"></script>
</body>
</html>
