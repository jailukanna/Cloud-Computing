
<?php

session_start();

if(isset($_GET['logout'])){

    //Simple exit message
    #$logout_message = "<div class='msgln'><span class='left-info'>User <b class='user-name-left'>". $_SESSION['name'] ."</b> has left the chat session.</span><br></div>";
    #file_put_contents("teacher_questions.html", $logout_message, FILE_APPEND | LOCK_EX);

    session_destroy();
    header("Location: index.php"); //Redirect the user To Main page
}



?>


<!DOCTYPE html>
<html lang="en">

<head>
    <title>
        Home Page
    </title>
    <meta charset="utf-8" http-equiv="referesh">
    <!-- This line will give the instruction on how the browser control the page how suppose to show the content in Tablet, Phone-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <link href="/css/stylesheet.css" type="text/css" rel="stylesheet">
    <link href="/css/responsive_setting.css" type="text/css" rel="stylesheet">
    <link href="/css/login_form.css" rel="stylesheet" type="text/css">

    <link href="/css/footer.css" type="text/css" rel="stylesheet">
    <link href="/css/userhomepage.css" type="text/css" rel="stylesheet">
    <!-- <meta http-equiv="refresh" content="12" > -->
    <link href="css/style2.css" rel="stylesheet">
    <style>
        body{
            background: url(https://placeimg.com/img/bg-2.svg) repeat;
        }
    </style>

    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>


</head>



<body>

<header>
    <nav class="navbar navbar-expand-lg navbar-dark navbar-light badge-dark " style="background-color:#04091e;">

        <div class="conatainer-fluid">
        </div>

        <div class=" conatainer-fluid" style="background-color:seagreen;">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon" ></span>
            </button>
        </div>



        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item p-4">

                </li>
                <li class="nav-item p-4">
                </li>

                <li class="nav-item p-4">
                </li>

            </ul>

        </div>


    </nav>
</header>





<div class="container">
    <br/>
    <!-- THIS FORM TO SEARCH FOR MAGNITUDE -->
    <div class="row justify-content-center" >
        <div class="col-12 col-md-10 col-lg-8" >
            <form class="card card-sm" action="switch.php" method="POST">

                <div class="card-body row no-gutters align-items-center">

                    <label for="name"><b style="color: navy">Your Name:</b></label>
                    <input class="form-control form-control-lg form-control-borderless" id="name" type="text"  name="name" required>
                    <br>

                    <label for="option"><b style="color: navy"> Want to be ?:</b></label>
                    <select class="custom-select d-block w-100" id="option"  required name="select">
                        <option></option>
                        <option value="Teacher">Teacher</option>
                        <option value="Admin">Admin</option>
                        <option value="Student">Student</option>
                    </select>
                </div>
                <br>

                <div class="col-auto">
                    <button class="btn btn-outline-success" type="submit" name="submit">Log in</button>
                </div>
            </form>
        </div>
        <!--end of col-->
    </div>
</div>





<footer class="container-fluid foot">
    <div class="container-fluid foot_div">
        <p class="h6 foot_text">Copyright &copy;2021 All rights reserved | This template is made with &#x1F498;by <span id="name">Aiman Abdullah</span> </p>
    </div>


</footer>


</body>

</html>

