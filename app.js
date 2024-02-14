function login(username, password) {
  if (username === "admin" && password === "password123") {
    localStorage.setItem("isLoggedIn", "true");
    alert("Login successful!");
    window.location.href = "dashboard.html";
  } else {
    alert("Invalid username or password.");
  }
}
