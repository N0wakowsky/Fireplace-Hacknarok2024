document.getElementById("codeInput").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        handleSubmit();
    }
});

function handleSubmit() {
    var code = document.getElementById("codeInput").value;
    if (code) {
        window.location.href = "fireplace/" + encodeURIComponent(code);
    } else {
        alert("Niepoprawny kod. Spróbuj ponownie.");
    }
}
