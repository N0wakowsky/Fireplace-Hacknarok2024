const socket = io.connect('http://' + document.domain + ':' + location.port);

function get_code(){
    let pathname = window.location.pathname;
    let parts = pathname.split('/');
    return parts[parts.length - 1];
}

socket.on('fireplace_closed', function(msg) {
    if(msg == get_code()) window.location.replace("/");
});


window.addEventListener('blur', function(event) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/user/out', false);
    xhr.send();
});


window.addEventListener('focus', function(event) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/user/in', false);
    xhr.send();
});