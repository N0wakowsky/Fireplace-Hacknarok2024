document.addEventListener('DOMContentLoaded', function() {
    var logoutButton = document.querySelector('.logout-button');
    logoutButton.addEventListener('click', function() {
        window.location.href = "/user/logout";
    });
});
