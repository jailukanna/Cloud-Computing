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
    <title>Student Page</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <link href="/css/footer.css" type="text/css" rel="stylesheet">
    <link href="/css/userhomepage.css" type="text/css" rel="stylesheet">
    <!-- <meta http-equiv="refresh" content="12" > -->
    <link href="css/style2.css" rel="stylesheet">

    <!-- These scripts for Socket IO Benefit -->
    <script type="text/javascript" src="//code.jquery.com/jquery-1.4.2.min.js"></script>
    <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js"></script>

    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript">
        // jQuery Document
        $(document).ready(function () {

            // This function when Teacher put question and click Submit
            $("#submit").click(function () {
                var clientmsg = $("#textarea").val();
                $.post("student_post.php", { text: clientmsg });
                $("#textarea").val("");
                return false;
            });



            // Load Teacher Question
            function loadLog() {
                // Put here id of container that show message
                var oldscrollHeight = $("#teacherQuestion")[0].scrollHeight - 20; //Scroll height before the request

                $.ajax({
                    url: "teacher_questions.html",
                    cache: false,
                    success: function (html) {
                        // Put here id of container that show message
                        $("#teacherQuestion").html(html); //Insert chat log into the #chatbox div

                        //Auto-scroll
                        // Put here id of container that show message
                        var newscrollHeight = $("#teacherQuestion")[0].scrollHeight - 20; //Scroll height after the request
                        if(newscrollHeight > oldscrollHeight){
                            // Put here id of container that show message
                            $("#teacherQuestion").animate({ scrollTop: newscrollHeight }, 'normal'); //Autoscroll to bottom of div
                        }
                    }
                });
            }

            setInterval (loadLog, 1000);





            // Load Admin Answer
            function loadLogg() {
                // Put here id of container that show message
                var old = $("#admin_answer")[0].scrollHeight - 20; //Scroll height before the request

                $.ajax({
                    url: "admin_answers.html",
                    cache: false,
                    success: function (html) {
                        // Put here id of container that show message
                        $("#admin_answer").html(html); //Insert chat log into the #chatbox div

                        //Auto-scroll
                        // Put here id of container that show message
                        var newscrol = $("#admin_answer")[0].scrollHeight - 20; //Scroll height after the request
                        if(newscrol > old){
                            // Put here id of container that show message
                            $("#admin_answer").animate({ scrollTop: newscrol }, 'normal'); //Autoscroll to bottom of div
                        }
                    }
                });
            }

            setInterval (loadLogg, 1000);










            // Put here id of button click to exit from chat (leave Game)
            $("#exit").click(function () {
                var exit = confirm("Are you sure you want to end the session?");

                    window.location = "index.php?logout=true";

            });
        });



        // Load Grade of Student
        $(document).ready(function(){
            setInterval(function(){
                $("#grade").load(window.location.href + " #grade" );
            }, 1000);
        });



        // Load Teacher name of Student
        $(document).ready(function(){
            setInterval(function(){
                $("#teacher").load(window.location.href + " #teacher" );
            }, 1000);
        });




    </script>








    <style>
        body{
            background: url(https://placeimg.com/img/bg-2.svg) repeat;
        }
    </style>



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
                <a class="nav-link logout active" id="exit" href="#"  style="color: lightblue;">Leave Game <span class="sr-only"></span></a>
            </li>

        </ul>
    </div>
</nav>





<div class="container-fluid">
    <div class="coloumn" id="namediv" style="margin-top: 2%">
        <h5 class="h5" style="text-align: left;color: #000000"><b>&#128102; Student name: </b><span style="color:blue; font-family: Arial"><?php echo $_SESSION['student']; ?></span> </h5>
        <h5 class="h5" style="text-align: left;color: #000000">&#128116; Teacher name: <span style="color:blue; font-family: Arial" id="teacher"> <?php if (isset($_SESSION['teacher']))  {echo $_SESSION['teacher'];} else{ echo "No Teacher Available";}?></span> </h5>
        <br>
    </div>
</div>
<hr>





<div class="container-fluid" >

    <h4 class="h4" style="text-align: left; color: black">The Question is : </h4>
    <br>
            <h3><i style="color: RED" id="teacherQuestion"> <?php
            if(file_exists("teacher_questions.html") && filesize("teacher_questions.html") > 0){
                $contents = file_get_contents("teacher_questions.html");
                echo $contents;
            }
            ?></i></h3>





    <hr>
    <h5 class="h5" style="text-align: left">&#128104; Admin Hints &#128073;
        <h3><i style="color: RED" id="admin_answer"> <?php
                if(file_exists("admin_answers.html") && filesize("admin_answers.html") > 0){
                    $contents = file_get_contents("admin_answers.html");
                    echo $contents;
                }
                ?></i></h3>


</div>
<hr>



<!-- THIS FORM TO SEARCH FOR MAGNITUDE -->
<div class="row justify-content-around">
    <div class="col-12 col-md-10 col-lg-6" style="background-color: #dad8d8;border-radius: 15px 50px; box-shadow: 10px 10px 5px #6059f6;">
        <form  method="POST" action="/student.php">

            <label for="textarea" class="form-label"><i style="color: blue;font-size: larger;"> Answer The Question:</i></label>
            <br>
            <textarea class="form-control" id="textarea" cols="30" rows="2" style="border:solid 1px black;"  name="answer" required placeholder="write something"></textarea>
            <br>
            <div class="col-auto">
                <button class="btn btn-outline-primary" type="submit" name="submit" id="submit">Submit</button>
                <br>
            </div>

        </form>

        <br>




    </div>
</div>


<hr>



<div class="container-fluid"style="border: none " >
    <h5 id="grade" class="h5" style="text-align: left;">You Get Grade: <i><?php
            if (isset($_SESSION['grade']))  {echo $_SESSION['grade'];}

            ?> %</i></h5>
    <br>

</div>


<footer class="foot">
    <div class="container-fluid foot_div">
        <p class="h6 foot_text">Copyright &copy;2021 All rights reserved | This template is made with &#x1F498;by <span id="name">Aiman Abdullah</span> </p>
    </div>


</footer>
</body>
</html>
