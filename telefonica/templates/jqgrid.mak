<%inherit file="local:templates.master"/>
<%def name="title()">
  Welcome to Telefonica
</%def>
<%def name="head_content()">

   <style type="text/css">
   </style>

   <script type="text/javascript">
        $(document).ready(function () {

            $("#jqGrid").jqGrid({
                url: 'http://trirand.com/blog/phpjqgrid/examples/jsonp/getjsonp.php?callback=?&qwery=longorders',
                mtype: "GET",
				styleUI : 'Bootstrap',
                datatype: "jsonp",
                colModel: [
                    { label: 'OrderID', name: 'OrderID', key: true, width: 75 },
                    { label: 'Customer ID', name: 'CustomerID', width: 150 },
                    { label: 'Order Date', name: 'OrderDate', width: 150 },
                    { label: 'Freight', name: 'Freight', width: 150 },
                    { label:'Ship Name', name: 'ShipName', width: 150 }
                ],
				viewrecords: true,
                height: 250,
                rowNum: 20,
                autowidth: true,
                pager: "#jqGridPager"
            });
        });

   </script>

</%def>
<!--main content start-->
<section id="main-content">

      <!-- page start-->

    <div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">
		<div class="row">
			<ol class="breadcrumb">
				<li><a href="#">
					<em class="fa fa-home"></em>
				</a></li>
				<li class="active">Widgets</li>
			</ol>
		</div><!--/.row-->
        <br>
		<div class="row">
            <div style="margin-left:10px">
            <table id="jqGrid"></table>
            <div id="jqGridPager"></div>
            </div>
		</div><!--/.row-->
        <br>
        <br>
      <!-- page end-->
</div>
  </section>
</section>

<%def name="bottom_scripts()">
</%def>
