document.getElementById('joinButton').addEventListener('click', function() {
    var codeInputValue = document.getElementById('code_input_create').value;
    window.location.href = '/fireplace/' + codeInputValue;
});

