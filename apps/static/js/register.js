$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;

	$('#name').blur(function() {
		check_user_name();
	});

	$('#password').blur(function() {
		check_pwd();
	});

	$('#re-password').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});


	function check_user_name(){
		var len = $('#name').val().length;
		if(len<5||len>20)
		{
			$('#name').next().html('请输入5-20个字符的用户名')
			$('#name').next().show();
			error_name = true;
		}
		else
		{
			var username = $('#name').val();
			var csrf = $('input[name="csrfmiddlewaretoken"]').val()
			// 当用户名符合要求进行用户名是否重名判断
			$.post('/user/register_check/',{'username': username, 'csrfmiddlewaretoken': csrf}, function (data) {
				if(data.res == 1){
					$('#name').next().html('用户名已存在');
					$('#name').next().show();
					error_name = true;
				}
				else {
					$('#name').next().hide();
					error_name = false;
				}
            })
		}
	}

	function check_pwd(){
		var len = $('#password').val().length;
		if(len<8||len>20)
		{
			$('#password').next().html('密码最少8位，最长20位')
			$('#password').next().show();
			error_password = true;
		}
		else
		{
			$('#password').next().hide();
			error_password = false;
		}		
	}


	function check_cpwd(){
		var pass = $('#password').val();
		var cpass = $('#re-password').val();

		if(pass!=cpass)
		{
			$('#password').next().html('两次输入的密码不一致')
			$('#password').next().show();
			error_check_password = true;
		}
		else
		{
			$('#re-password').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	}


	$('#reg_form2').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false)
		{

		   // 当点击submit时将密码加密
			$('#password').val(hex_sha1($('#password').val()));
            $('#re-password').val(hex_sha1($('#re-password').val()));

			return true;
		}
		else
		{
			return false;
		}

	});



});
