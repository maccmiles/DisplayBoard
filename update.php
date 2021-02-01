<?php
$servername = "localhost";
$username = "********";
$password = "********";
$dbname = "********";
$status = ($_GET["change"]);
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = sprintf("UPDATE Requests SET Commands = '%s'", $status);

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