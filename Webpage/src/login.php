<?php
include("config.php");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["login-username"];
    $password = $_POST["login-password"];

    // Retrieve user data from the database
    $sql = "SELECT id, username, password FROM users WHERE username=?";
    $stmt = $mysqli->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();
    $stmt->bind_result($id, $username, $hashed_password);

    if ($stmt->num_rows == 1 && password_verify($password, $hashed_password)) {
        session_start();
        $_SESSION["user_id"] = $id;
        $_SESSION["username"] = $username;
        header("location: welcome.php"); // Redirect to a welcome page after successful login
    } else {
        echo "Login failed. Please check your username and password.";
    }

    $stmt->close();
}

$mysqli->close();
?>
