<?php

// Enable error reporting for debugging
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Start session if needed
if (session_status() == PHP_SESSION_NONE) {
    session_start();
}

// Define function for debugging
function debug($var) {
    echo "<pre>";
    print_r($var);
    echo "</pre>";
}

// Access GET parameters
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    debug($_GET);
}

// Access POST parameters
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    debug($_POST);
}

// Access FILES parameters
if (!empty($_FILES)) {
    debug($_FILES);
}

// run with php -S 127.0.0.1:8000 debug_server.php, send requests to http://127.0.0.1:8000/debug_server.php

?>

