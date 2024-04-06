document.getElementById("codeInput").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        handleSubmit();
    }
});

function handleSubmit() {
    var code = document.getElementById("codeInput").value;
    if (code === "12345") {
        window.location.href = "/main";
    } else {
        alert("Niepoprawny kod. Spróbuj ponowe.");
    }
}
