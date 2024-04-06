document.addEventListener('click', function() {
    var registerbutton = document.querySelector('.register_button')
    registerbutton.addEventListener('click', function() {
        window.location.href = "/auth/register"
    })
})
