<?php
$host = "localhost"; // MySQL server host
$username = "your_username"; // MySQL username
$password = "your_password"; // MySQL password
$database = "your_database"; // MySQL database name

// Create a database connection
$mysqli = new mysqli($host, $username, $password, $database);

// Check connection
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}
?>
