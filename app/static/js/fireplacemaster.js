document.getElementById('leaveButton').addEventListener('click', function get_code(){
    let pathname = window.location.pathname;
    let parts = pathname.split('/');
    window.location.href = "/api/fireplace/" + parts[parts.length - 1] + "/leave";
});