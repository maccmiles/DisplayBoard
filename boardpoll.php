<?php
$con=mysqli_connect("localhost","********","********","********");
// Check connection
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$result = mysqli_query($con,"SELECT * FROM Requests");
?>
 <?php
while($row = mysqli_fetch_array($result))
{
echo $row['Commands'];
}
mysqli_close($con);
?>