const socket = io.connect('http://' + document.domain + ':' + location.port);

function get_code(){
    let pathname = window.location.pathname;
    let parts = pathname.split('/');
    return parts[parts.length - 1];
}

socket.on('update', function(msg) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/fireplace/' + get_code() + '/get_users', false);
    
    xhr.send(null);

    let data = JSON.parse(xhr.responseText)

    let list = document.querySelector("#users");

    while (list.firstChild) list.removeChild(list.firstChild);

    data.forEach(element => {
        var row = document.createElement("li");

        row.textContent = element[0];
        row.setAttribute("active", element[1]);
        list.appendChild(row);
    });
});