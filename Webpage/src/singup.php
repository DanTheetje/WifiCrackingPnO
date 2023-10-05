<?php
include("config.php");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["signup-username"];
    $email = $_POST["signup-email"];
    $password = password_hash($_POST["signup-password"], PASSWORD_DEFAULT); // Hash the password

    // Insert user data into the database
    $sql = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)";
    $stmt = $mysqli->prepare($sql);
    $stmt->bind_param("sss", $username, $email, $password);

    if ($stmt->execute()) {
        echo "Registration successful. You can now <a href='login.html'>log in</a>.";
    } else {
        echo "Error: " . $stmt->error;
    }

    $stmt->close();
}

$mysqli->close();
?>
