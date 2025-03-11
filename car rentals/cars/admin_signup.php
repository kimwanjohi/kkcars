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

// Your HTML form submission handling
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve data from the HTML form
    $staff_id = $_POST['staff_id'];
    $email = $_POST['email'];
    $username = $_POST['username'];
    $pwd = $_POST['pwd'];

	
// SQL query to insert data into the database
    $sql = "INSERT INTO admin_login (staff_id, email, username, pwd) VALUES('$staff_id', '$email', '$username', '$pwd')";
    
    if ($conn->query($sql) === TRUE) {
        $_SESSION['form_msg'] = "Sign up successfull!";
        header("location: admin_login.html");
        exit();
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;

    }
}

// Close the connection
$conn->close();
?>
  