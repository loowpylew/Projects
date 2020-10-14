<?php

if (filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)){

if(isset($_POST['submit'])) {
  $name= $_POST['name']; /*This will store the name of the user*/ 
  $visitor_email = $_POST['email']; /*This will store the email id of the user*/ 
  $subject = $_POST['subject'];
  $message = $_POST['message']; /*This will store the message*/ 

  
  $mailTo =  "theworksSE@outlook.com";
  $headers = "From: ".$visitor_email;  /* reply to */
  $txt = "You have recieved an email from ".$name."\n\n".$message; 
  mail($mailTo, $subject, $txt, $headers);
  header("Location: index.html?mailsend");
}
}
?> 