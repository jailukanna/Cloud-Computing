<?php


session_start();



if(isset($_POST['submit'])){

    if($_POST['name'] != ""){
        $name = stripslashes(htmlspecialchars($_POST['name']));


        if ($_POST['select'] =='Teacher'){
            $_SESSION['teacher'] = $name;
            header("Location: teacher.php"); //Redirect the Teacher page

        }


        if ($_POST['select'] =='Student'){
            $_SESSION['student'] = $name;
            header("Location: student.php?user=".$_SESSION['student']); //Redirect the Student Page
        }


        if ($_POST['select'] =='Admin'){
            $_SESSION['admin'] = $name;
            header("Location: admin.php?user=".$_SESSION['admin'] ); //Redirect the Admin page
        }




    }

}



?>

