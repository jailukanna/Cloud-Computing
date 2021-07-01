$(document).ready(function() {
    // timer function
    function startTimer(duration, display) {
        var timer = duration, minutes, seconds;
        var refresh = setInterval(function () {
            minutes = parseInt(timer / 60, 10)
            seconds = parseInt(timer % 60, 10);

            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;

            var output = minutes + " : " + seconds;
            display.text(output);
            $("title").html(output + " - TimerTimer");



            if (--timer < 0) {
                //display.text("Time's Up!");
                clearInterval(refresh);  // exit refresh loop
            }


        }, 1000);

    }

    // start timer
    jQuery(function ($) {
        var display = $('#time');
        startTimer(Seconds, display);
    });
})


// ====================================== DIV Contents Update Section ========================================//

    // Refresh part of page not all


/*
$(document).ready(function(){
setInterval(function(){
      $("#tablediv").load(window.location.href + " #tablediv" );
}, 8000);
});






$(document).ready(function(){
setInterval(function(){
      $("#names").load(window.location.href + " #names" );
}, 8000);
});



$(document).ready(function(){
setInterval(function(){
      $("#studentanswer").load(window.location.href + " #studentanswer" );
}, 8000);
});


$(document).ready(function(){
setInterval(function(){
      $("#namediv").load(window.location.href + " #namediv" );
}, 8000);
});




$(document).ready(function(){
setInterval(function(){
      $("#teacherQuestion").load(window.location.href + " #teacherQuestion" );
}, 8000);
});


*/








