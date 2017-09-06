$(document).ready(function () {
    $('.name_input').blur(function () {
        let len = $(this).val().length;
        if (len === 0) {
            $('.error_name').html("请填写用户名").show()
        } else {
            $('.error_name').hide()
        }
    });

    $('.pass_input').blur(function () {
        let len = $(this).val().length;
        if (len === 0) {
            $('.error_pwd').html("请填写用户名").show()
        } else {
            $('.error_pwd').hide()
        }
    });
});