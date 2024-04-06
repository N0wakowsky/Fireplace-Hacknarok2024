document.addEventListener('DOMContentLoaded', function() {
    var logoutButton = document.querySelector('.stats-button');
    logoutButton.addEventListener('click', function() {
        window.location.href = "/statistics";
    });
});