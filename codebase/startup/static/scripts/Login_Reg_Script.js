$(document).ready(function(){
	$("#trigger").click(function(){
		
		var loginOpen = document.getElementById('id_loginOpen').value ;
		var registerOpen = document.getElementById('id_registerOpen').value ;
		var completelyClosed = loginOpen=='False' && registerOpen=='False' ;
		var completelyOpen = loginOpen=='True' && registerOpen=='True' ;
		if (completelyClosed)	{
			/*code for opening box - as loginOpen=False*/
			
			
			$("#form_login").css('display','block');
			$("#form_reg").css('display','none');
			$("#login_box").slideDown(200);
			
			document.getElementById('id_loginOpen').setAttribute('value',"True");
		} else if (completelyOpen)	{


			document.getElementById('id_loginOpen').setAttribute('value',"True");
			document.getElementById('id_registerOpen').setAttribute('value',"False");
			/*code for opening box - as loginOpen=False*/
			
			$("#form_login").css('display','block');
			$("#form_reg").css('display','none');
			$("#login_1st").focus();



		}	else if (loginOpen == 'True')	{
			
			document.getElementById('id_loginOpen').setAttribute('value',"False");
			document.getElementById('id_registerOpen').setAttribute('value',"False");
			
			/*code for closing box - as loginOpen=True*/
			
			$("#login_box").slideUp(200);
		} else {
			/*this is the case when registerOpen is true and loginOpen is false. 
				ie register mode was open, but now login is pressed.
				so change the form from register to login - dont drop or rise the box, its already open*/
			document.getElementById('id_loginOpen').setAttribute('value',"True");
			document.getElementById('id_registerOpen').setAttribute('value',"False");
			/*code for opening box - as loginOpen=False*/
			
			$("#form_login").css('display','block');
			$("#form_reg").css('display','none');
			$("#login_1st").focus();
		}
	});
		
	$("#reg_btn").click(function(){
		
		var loginOpen = document.getElementById('id_loginOpen').value ;
		var registerOpen = document.getElementById('id_registerOpen').value ;
		var completelyClosed = loginOpen=='False' && registerOpen=='False' ;
		
		if (completelyClosed)	{
			/*code for opening box - as loginOpen=False*/
			
			$("#form_login").css('display','none');
			$("#form_reg").css('display','block');
			$("#login_box").slideDown(200);
			document.getElementById('id_registerOpen').setAttribute('value',"True");
		} else if (registerOpen == 'True')	{
				
				document.getElementById('id_registerOpen').setAttribute('value',"False");
				document.getElementById('id_loginOpen').setAttribute('value',"False");
				loginOpen.value = 'False';
				
				/*code for closing box - as loginOpen=True*/
				
				$("#login_box").slideUp(200);
		} else {
				
				/*this is the case when loginOpen is true and registerOpen is false. 
				ie login mode was open, but now register is pressed.
				so change the form from login to register*/
				document.getElementById('id_registerOpen').setAttribute('value',"True");
				
				/*code for opening box - as loginOpen=False*/
				
				$("#form_login").css('display','none');
				$("#form_reg").css('display','block');
				$("#login_box").slideDown(200);
			
			
		}
		
		/*
		$("#form_login").css('display','none');
		$("#form_reg").css('display','block');
		$("#Reg_1st").focus();
	$("#reg_btn").click(function(){
		$("#login_box").slideUp(200);
		$("#form_login").css('display','none');
		$("#form_reg").css('display','none');
	$("#reg_btn").click(function(){
		$("#login_box").slideDown(200,function(){
		$("#form_login").css('display','none');
		$("#form_reg").css('display','block');
	
		 });
		});*/
	  });
	});
	  