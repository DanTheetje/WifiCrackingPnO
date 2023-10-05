<?php
session_start();

// Check if the user is logged in, if not, redirect to the login page
if (!isset($_SESSION["user_id"]) || empty($_SESSION["user_id"])) {
    header("location: login.html");
    exit;
}

// If the user is logged in, you can display a welcome message with their username
$username = $_SESSION["username"];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
        }

        .container {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h2 {
            text-align: center;
        }

        .welcome-message {
            text-align: center;
            margin-top: 20px;
        }

        .logout-link {
            text-align: center;
            margin-top: 20px;
        }

        a {
            color: #007bff;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Welcome, <?php echo htmlspecialchars($username); ?>!</h2>
        <div class="welcome-message">
            Welcome to our website. You are now logged in.
        </div>
        <div class="logout-link">
            <a href="logout.php">Log out</a>
        </div>
    </div>
</body>
</html>
