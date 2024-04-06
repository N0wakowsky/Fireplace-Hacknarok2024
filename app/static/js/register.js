document.getElementById("loginForm").addEventListener("submit", function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();
    
    // Get the values of nickname and password
    var nickname = document.getElementById("nickname").value;
    var password = document.getElementById("password").value;
    
    // Check if both fields are filled
    if (nickname && password) {
      // Redirect to a new page
      window.location.href = "your-new-page.html";
    } else {
      alert("Please fill in both fields!");
    }
})