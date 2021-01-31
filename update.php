<?php
$servername = "localhost";
$username = "*****";
$password = "*****";
$dbname = "*****";
// Switch Case
// Availible Phrases: "Set the display to $" 
// "I'll $"
// "I'm $"
switch ($_GET["change"]) {
    case "duty":
        $status = "0";
        break; 
    case "on duty":
        $status = "0";
        break;
    case "class":
        $status = "1";
        break;
    case "in class":
        $status = "1";
        break;
    case "going to class":
        $status = "1";
        break;
    case "out and about":
        $status = "2";
        break;
    case "going out and about":
        $status = "2";
        break;
    case "working":
        $status = "3";
        break;
    case "here":
        $status = "4";
        break;
    case "sleep":
        $status = "5";
        break;
    case "sleeping":
        $status = "5";
        break;
    case "going to sleep":
        $status = "5";
        break;
    case "going to bed":
        $status = "5";
        break;
    case "at an event":
        $status = "6";
        break;
    case "heading to an event":
        $status = "6";
        break;
    case "going an event":
        $status = "6";
        break;
    case "off campus":
        $status = "7";
        break;
    case "off - campus":
        $status = "7";
        break;
    case "meeting":
        $status = "8";
        break;
    case "at a meeting":
        $status = "8";
        break;
    case "in a meeting":
        $status = "8";
        break;
    case "going to a meeting":
        $status = "8";
        break;
    case "brb":
        $status = "9";
        break;
    case "be right back":
        $status = "9";
        break;
    default;
        $status = "9";
        break;
}
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = sprintf("UPDATE Status SET Mode = %s WHERE Request = 'Update'", $status);

if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
} else {
    echo "Error updating record: " . $conn->error;
}

$conn->close();
//Log last request to file [debug]
$fp = fopen('log.txt', 'w');
fwrite($fp, $_GET["change"]);
fclose($fp);
?>
