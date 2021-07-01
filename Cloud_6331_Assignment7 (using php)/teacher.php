<?php

session_start();

if(isset($_GET['logout'])){

    //Simple exit message
    //$logout_message = "<div class='msgln'><span class='left-info'>User <b class='user-name-left'>". $_SESSION['name'] ."</b> has left the chat session.</span><br></div>";
    //file_put_contents("exitUSER.html", $logout_message,  LOCK_EX);

    session_destroy();
    header("Location: index.php"); //Redirect the user To Main page
}









if (isset($_POST['grade'])){
    $_SESSION['grade'] = $_POST['grade'];  // Hold Current Grade

}


?>


<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <title>Teacher Page</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <link href="/css/footer.css" type="text/css" rel="stylesheet">
    <link href="/css/userhomepage.css" type="text/css" rel="stylesheet">
    <!-- <meta http-equiv="refresh" content="12" > -->
    <link href="css/style2.css" rel="stylesheet">

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

<style>
    body{
        background: url(https://placeimg.com/img/bg-2.svg) repeat;

    }
</style>

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
                <a class="nav-link active" href="/index.php" style="color: lightblue;">Home Page <span class="sr-only">(current)</span></a>
            </li>

            <li class="nav-item p-4">

                <input type="hidden" class="logout"><a class="nav-link active" id="exit" href="#"  style="color: lightblue;">Leave Game</a></input>
            </li>
        </ul>
    </div>
</nav>





<div class="container-fluid" id="names" style="margin-top: 12px">
    <h5 class="h5" style="text-align: left;color: #000000"><b>&#128116; Teacher name: </b><span style="color:blue; font-family: Arial"><?php echo $_SESSION['teacher']; ?></span> </h5>
  <h5 class="h5" style="text-align: left;color: #000000">&#128102; Student name: <span style="color:blue; font-family: Arial" id="teacher"><?php  if (isset($_SESSION['student']))  {echo $_SESSION['student'];} else{ echo "No Student Available";} ?></span> </h5>
</div>

<hr>


<div class="container">

    <!-- THIS FORM TO SEARCH FOR MAGNITUDE -->
    <div class="row justify-content-around">
        <div class="col-12 col-md-10 col-lg-8" style="background-color: #dad8d8;border-radius: 15px 50px; box-shadow: 10px 10px 5px #6059f6;">
            <!-- This Action mean call function of teacher page -->
            <form  method="POST" action="/teacher.php">
                <label for="textarea" class="form-label"><b style="color: blue;font-size: larger;"> Enter Question:</b></label>
                <br>
                <textarea class="form-control" id="textarea"  cols="40" rows="2" style="border:solid 1px black;"  name="question"  required autocomplete="true" autofocus></textarea>

                <br>
                <div class="col-auto">
                    <button class="btn btn-outline-primary" type="submit" name="submit" id="submit"  value="form1">Submit</button>
                </div>
                <br>
            </form>
        </div>

    </div>
</div>

<br>
<hr>
<br>


<div  style="margin-left:1%; position: static; float: end" >
    <h4 class="h4" style="text-align: left; color: black">Student Answer : </h4>
    <br>

    <h3><i style="color: RED" id="student_answers"> <?php
            if(file_exists("student_answers.html") && filesize("student_answers.html") > 0){
                $contents = file_get_contents("student_answers.html");
                echo $contents;
            }
            ?></i></h3>

</div>


<div class="container"style="position:relative; float:right;">
    <form method="post" action="/teacher.php">
        <label for="grade" class="label"><i>&#128221; Grade The Answer</i></label>
        <select class="d-block w-10" id="grade"  required name="grade">
            <option>0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
        </select>

        <br>

        <button class="btn btn-sm btn-outline-info" type="submit" name="submit">Grade it</button>
    </form>
    <hr>
</div>
<br>


<footer class="foot">
    <div class="container-fluid foot_div">
        <p class="h6 foot_text">Copyright &copy;2021 All rights reserved | This template is made with &#x1F498;by <span id="name">Aiman Abdullah</span> </p>
    </div>


</footer>

</body>
</html>

