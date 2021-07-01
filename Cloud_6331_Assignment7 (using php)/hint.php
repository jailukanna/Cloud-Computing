<?php
session_start();

?>

<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <title>Hint page</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <link href="/static/css/footer.css" type="text/css" rel="stylesheet">
    <link href="/static/css/userhomepage.css" type="text/css" rel="stylesheet">
    <!-- <meta http-equiv="refresh" content="10" > -->
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>


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
                <a class="nav-link active" href="/admin.php" style="color: lightblue;">admin page <span class="sr-only">(current)</span></a>
            </li>


        </ul>
    </div>
</nav>





<br/>
<!-- THIS FORM TO SEARCH FOR MAGNITUDE -->
<div class="row justify-content-center" >

    <h4 class="h4">Student need Help For this Question:  <i style="color: RED" id="admin_answers"> <?php


    if(file_exists("teacher_questions.html") && filesize("teacher_questions.html") > 0){
        $contents = file_get_contents("teacher_questions.html");
        echo $contents;
    }



 ?></i></h4>

</div>

<br>

<script type="text/javascript">
    // jQuery Document
    $(document).ready(function () {

        // This function when Admin put Answer and click Submit
        $("#submit").click(function () {
            var clientmsg = $("#textarea").val();
            $.post("admin_post.php", { text: clientmsg });
            $("#textarea").val("");
            return false;
        });

        // This Function will load data from url: "teacher_questions.html",  and show it in the place that have id "admin_answers"
        function loadLog() {
            // Put here id of container that show message
            var oldscrollHeight = $("#admin_answers")[0].scrollHeight - 20; //Scroll height before the request

            $.ajax({
                url: "teacher_questions.html",
                cache: false,
                success: function (html) {
                    // Put here id of container that show message
                    $("#admin_answers").html(html); //Insert chat log into the #chatbox div

                    //Auto-scroll
                    // Put here id of container that show message
                    var newscrollHeight = $("#admin_answers")[0].scrollHeight - 20; //Scroll height after the request
                    if(newscrollHeight > oldscrollHeight){
                        // Put here id of container that show message
                        $("#admin_answers").animate({ scrollTop: newscrollHeight }, 'normal'); //Autoscroll to bottom of div
                    }
                }
            });
        }

        setInterval (loadLog, 1000);

        // Put here id of button click to exit from chat (leave Game)
        $("#exit").click(function () {
            var exit = confirm("Are you sure you want to end the session?");
            if (exit == true) {
                window.location = "index.php?logout=true";
            }
        });
    });
</script>


<div class="row justify-content-center" style="margin-top: 5%">
    <div class="col-12 col-md-10 col-lg-6" style="background-color: #dad8d8">
        <form  method="POST" action="/hint.php">

            <label for="textarea" class="form-label"><b style="color: blue;font-size: larger;"> Answer The Question:</b></label>
            <br>
            <textarea class="form-control" id="textarea" cols="40" rows="2" style="border:solid 1px black;"  name="answer" required placeholder="write something"></textarea>
            <br>
            <div class="col-auto">
                <button class="btn btn-outline-primary" type="submit" name="submit" id="submit">Send a Hint</button>
            </div>
            <hr>
        </form>
    </div>
</div>



</body>
</html>

