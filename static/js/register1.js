$(document).ready(function () {
    let is_user_name = false;
    let is_pwd = false;
    let is_cpwd = false;
    let is_email = false;
    let is_argree = false;

    $('#user_name').blur(function () {
        check_user()
    });

    $("#pwd").blur(function () {
        check_pwd()
    });

    $('#cpwd').blur(function () {
        check_cpwd()

    });

    $("#email").blur(function () {
        check_email()
    });

    $("#allow").click(function () {
        if ($(this).attr('check')) {
            is_argree = true;
            $(this).siblings('span').hide();
        } else {
            $(this).siblings("span").html("请勾选同意");
            $(this).siblings("span").show();
            is_argree = false;
        }
    });

    function check_email() {
        var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

        if (re.test($('#email').val())) {
            $('#email').next().hide();
            is_email = true;
        }
        else {
            $('#email').next().html('你输入的邮箱格式不正确')
            $('#email').next().show();
            is_email = false;
        }

    }

    function check_cpwd() {
        let cpwd = $("#cpwd");
        let pwd = cpwd.val();
        if (pwd === $("#pwd").val()) {
            cpwd.next().hide();
            is_cpwd = true;
        } else {
            cpwd.next().html('两次密码输入不一致');
            cpwd.next().show();
            is_cpwd = false;
        }
    }

    function check_pwd() {
        let pwd = $('#pwd');
        let len = pwd.val().length;
        if (len < 6 || len > 20) {
            pwd.next().html('请输入6-20位密码');
            pwd.next().show();
            is_pwd = false;
        } else {
            pwd.next().hide();
            is_pwd = true;
        }
    }

    function check_user() {
        let user_name = $('#user_name');
        let len = user_name.val().length;
        if (len < 5 || len > 20) {
            user_name.next().html('请输入5-20个字符的用户名');
            user_name.next().show();
            is_user_name = false;
        } else {
            $.get("/user/register_exist/?uname=" + user_name.val(), function (data,status) {
                if (data.count > 0) {
                    user_name.next().html('账户已经存在').show();
                    is_user_name = false;
                } else {
                    is_user_name = true;
                    user_name.next().hide();
                }
            });
        }
    }

    $("#reg_sub").submit(function () {
        check_user();
        check_pwd();
        check_cpwd();
        check_email();

        return is_user_name && is_pwd && is_cpwd && is_email && is_argree;
    });
});
