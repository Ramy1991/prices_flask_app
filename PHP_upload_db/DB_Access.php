<?php
// $servername = "fdb21.awardspace.net";
// $username = "2757812_bprice";
// $password = "offer0000";
// $dbname = "2757812_bprice";

$con = mysqli_init(); 

$con->ssl_set($con, NULL, NULL, "DigiCertGlobalRootG2.crt.pem", NULL, NULL); 
$conn = mysqli_real_connect($con, "prices-app.mysql.database.azure.com", "admin1991@prices-app", "Ramy1991", "prices_test", 3306);

// $conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
mysqli_set_charset($conn, "utf8");


