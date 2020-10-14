<?php

$server="sql101.epizy.com";
$username="epiz_26448800";
$password="JKGwabzXweW";
$dbname="epiz_26448800_lewistaylorSE";

$conn = mysqli_connect($server,$username,$password,$dbname);

if(!$conn){
    die("Connection Failed:".mysqli_connect_error());
}
?>