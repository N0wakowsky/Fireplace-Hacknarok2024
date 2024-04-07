window.addEventListener('blur', function(event) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/user/out', true);
    xhr.send();
});