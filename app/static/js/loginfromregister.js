document.addEventListener('click', function() {
    var registerbutton = document.querySelector('.login_button')
    registerbutton.addEventListener('click', function() {
        window.location.href = "/auth/login"
    })
})