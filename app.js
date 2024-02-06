// Example code with security vulnerabilities

// Vulnerability 1: Cross-Site Scripting (XSS)
function displayMessage(message) {
  document.getElementById("output").innerHTML = message; // Potential XSS vulnerability
}

// Vulnerability 2: SQL Injection
function getUserData(username) {
  var query = "SELECT * FROM users WHERE username = '" + username + "'"; // SQL query with input concatenation
  // Execute query and return results
}

// Vulnerability 3: Insecure random number generation
function generateToken() {
  var token = Math.random(); // Insecure random number generation
  return token;
}

// Vulnerability 4: Insecure password hashing
function hashPassword(password) {
  return md5(password); // Using weak hashing algorithm MD5
}

// Vulnerability 5: Access control issue
var isAdmin = false;

function deleteUserData(username) {
  if (isAdmin) {
    // Delete user data
  } else {
    throw new Error("Access denied"); // Access control issue
  }
}
