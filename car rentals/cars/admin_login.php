<?php
session_start();

// Database credentials
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "car_rental_admin";

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// HTML form submission handling
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve data from the HTML form
    $username = $_POST['username'];
    $pwd = $_POST['pwd'];

    // Use prepared statements to prevent SQL injection
    $sql = "SELECT * FROM admin_login WHERE username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username); // "s" means string
    $stmt->execute();
    $result = $stmt->get_result();

    // Check if a user was found
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();

        // Validate the password (assuming it is stored as plain text; ideally use password_verify)
        if ($pwd === $row['pwd']) { // Replace with password_verify($pwd, $row['pwd']) if hashed
            // Store user details in the session
            $_SESSION['username'] = $row['username'];

            // Redirect to the admin page
            header("Location: view_cars_admin.php");
            exit();
        } else {
            // Invalid password
            $_SESSION['login_error'] = "Invalid password.";
            header("Location: login.html"); // Redirect back to login page
            exit();
        }
    } else {
        // Username not found
        $_SESSION['login_error'] = "Invalid username.";
        header("Location: login.html"); // Redirect back to login page
        exit();
    }

    // Close the prepared statement
    $stmt->close();
} else {
    echo "Form not submitted.";
}

// Close the connection
$conn->close();
?>
