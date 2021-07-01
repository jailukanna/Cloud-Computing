<?php
session_start();
if(isset($_SESSION['admin'])){
    $text = $_POST['text'];
    #date_default_timezone_set("America/Dallas");
    #$text_message = "<div class='msgln'><span class='chat-time'>".date("h:i:sa")."</span> <b class='user-name'>".$_SESSION['name']."</b> ".stripslashes(htmlspecialchars($text))."<br></div>";


    $text_message = "<div class='msgln'>".stripslashes(htmlspecialchars($text))."<br></div>";


    file_put_contents("admin_answers.html", $text_message, LOCK_EX); // Write Teacher Question to a file called teacher_questions.html


    #file_put_contents("teacher_questions.html", $text_message, FILE_APPEND | LOCK_EX);
}
?>