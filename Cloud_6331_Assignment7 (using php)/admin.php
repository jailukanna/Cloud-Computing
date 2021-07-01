<?php

session_start();

if(isset($_GET['logout'])){

    //Simple exit message
    //$logout_message = "<div class='msgln'><span class='left-info'>User <b class='user-name-left'>". $_SESSION['name'] ."</b> has left the chat session.</span><br></div>";
    //file_put_contents("exitUSER.html", $logout_message, FILE_APPEND | LOCK_EX);


    session_destroy();
    header("Location: index.php"); //Redirect the user To Main page
}



?>


<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <title>Admin Page</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <link href="/css/footer.css" type="text/css" rel="stylesheet">
    <link href="/css/userhomepage.css" type="text/css" rel="stylesheet">

    <link href="css/style2.css" rel="stylesheet">


    <style>
        body{
            background: url(https://placeimg.com/img/bg-2.svg) repeat;
        }
    </style>

    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript">
        // jQuery Document
        $(document).ready(function () {

            // This function when Teacher put question and click Submit
            $("#submit").click(function () {
                var clientmsg = $("#textarea").val();
                $.post("teacher_post.php", { text: clientmsg });
                $("#textarea").val("");
                return false;
            });

            // This Function will load data from txt file to the page
            function loadLog() {
                // Put here id of container that show message
                var oldscrollHeight = $("#student_answers")[0].scrollHeight - 20; //Scroll height before the request

                $.ajax({
                    url: "student_answers.html",
                    cache: false,
                    success: function (html) {
                        // Put here id of container that show message
                        $("#student_answers").html(html); //Insert chat log into the #chatbox div

                        //Auto-scroll
                        // Put here id of container that show message
                        var newscrollHeight = $("#student_answers")[0].scrollHeight - 20; //Scroll height after the request
                        if(newscrollHeight > oldscrollHeight){
                            // Put here id of container that show message
                            $("#student_answers").animate({ scrollTop: newscrollHeight }, 'normal'); //Autoscroll to bottom of div
                        }
                    }
                });
            }

            setInterval (loadLog, 1000);



            // Load Teacher name of Student
            $(document).ready(function(){
                setInterval(function(){
                    $("#teacher").load(window.location.href + " #teacher" );
                }, 1000);
            });









            // Put here id of button click to exit from chat (leave Game)
            $("#exit").click(function () {
                var exit = confirm("Are you sure you want to end the session?");
                if (exit == true) {
                    window.location = "index.php?logout=true";
                }
            });
        });
    </script>
</head>
<body>

<!-- NAVIGATION  -->
<nav class="navbar navbar-expand-lg navbar-dark navbar-light badge-dark " style="background-color:#04091e;">
    <div class=" conatainer-fluid" style="background-color:seagreen;">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon" ></span>
        </button>
    </div>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">

            <li class="nav-item p-4">
                <a class="nav-link active" href="/index.php" style="color: lightblue;">Home page <span class="sr-only">(current)</span></a>
            </li>

            <li class="nav-item p-4">
                <a class="nav-link logout active " id="exit" href="#" style="color: lightblue;">Leave Game <span class="sr-only"></span></a>
            </li>
        </ul>

    </div>
</nav>




<br>
<br>
<a class="restButton"  href="/hint.php" style="color: #04091e; margin: 0% 42%; text-align: center;width: 250px">Check if Student need Help</a>

<div class="container-fluid" id="tablediv" style="margin-top:50px">

    <table class="table table-bordered">
        <thead>

        <tr >
            <th style="font-size: xx-large;color:  #0a0a0a;text-align:center;">Teacher Questions &#128520;</th>
            <th style="font-size: xx-large;color:  #0a0a0a;text-align:center;">&</th>
            <th style="font-size: xx-large;color:  #0a0a0a;text-align:center;"> Student Answers &#128517;</th>


        </tr>

        </thead>

        <tbody>


        <tr>
            <td style="color:#cc0000;text-align:center;"><b>
                    <h3><i style="color: RED" id="teacherQuestion"> <?php
                            if(file_exists("teacher_questions.html") && filesize("teacher_questions.html") > 0){
                                $contents = file_get_contents("teacher_questions.html");
                                echo $contents;
                            }
                            ?></i></h3>
                </b></td>

            <td style="font-size: xx-large;color:  #0a0a0a;text-align:center;">&</td>


            <td style="color:#595cf6;text-align:center;"><b>
                    <h3><i style="color: RED" id="student_answers"> <?php
                            if(file_exists("student_answers.html") && filesize("student_answers.html") > 0){
                                $contents = file_get_contents("student_answers.html");
                                echo $contents;
                            }
                            ?></i></h3>
                </b></td>


        </tr>
        </tbody>

    </table>

</div>







<br>
<br>
<br>
<footer class="foot">
    <div class="container-fluid foot_div">
        <p class="h6 foot_text">Copyright &copy;2021 All rights reserved | This template is made with &#x1F498;by <span id="name">Aiman Abdullah</span> </p>
    </div>


</footer>


</body>
</html>

