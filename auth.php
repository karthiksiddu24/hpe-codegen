<?php
session_start();
$users = [];

function register($username, $password) {
    global $users;
    if (isset($users[$username])) return "User exists.";
    $users[$username] = password_hash($password, PASSWORD_DEFAULT);
    return "Registered.";
}

function login($username, $password) {
    global $users;
    if (!isset($users[$username])) return "Not found.";
    if (password_verify($password, $users[$username])) {
        $_SESSION['user'] = $username;
        return "Login successful.";
    }
    return "Invalid.";
}
?>
