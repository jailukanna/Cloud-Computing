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


$(document).ready(function(){
setInterval(function(){
      $("#tablediv").load(window.location.href + "#tablediv" );
}, 10000);
});






$(document).ready(function(){
setInterval(function(){
      $("#names").load(window.location.href + "#names" );
}, 10000);
});


$(document).ready(function(){
setInterval(function(){
      $("#namess").load(window.location.href + "#namess" );
}, 10000);
});



$(document).ready(function(){
setInterval(function(){
      $("#studentanswer").load(window.location.href + "#studentanswer" );
}, 10000);
});


$(document).ready(function(){
setInterval(function(){
      $("#namediv").load(window.location.href + "#namediv" );
}, 10000);
});


$(document).ready(function(){
setInterval(function(){
      $("#teachnamediv").load(window.location.href + "#teachnamediv" );
}, 10000);
});



$(document).ready(function(){
setInterval(function(){
      $("#adminhints").load(window.location.href + "#adminhints" );
}, 10000);
});





$(document).ready(function(){
setInterval(function(){
      $("#teacherQuestion").load(window.location.href + "#teacherQuestion" );
}, 10000);
});




$(document).ready(function(){
setInterval(function(){
      $("#grades").load(window.location.href + "#grades" );
}, 10000);
});



$(document).ready(function(){
setInterval(function(){
      $("#totalgrades").load(window.location.href + "#totalgrades" );
}, 10000);
});



$(document).ready(function(){
setInterval(function(){
      $("#averagegrades").load(window.location.href + "#averagegrades" );
}, 10000);
});


$(document).ready(function(){
setInterval(function(){
      $("#teQuestion").load(window.location.href + "#teQuestion" );
}, 10000);
});


$(document).ready(function(){
setInterval(function(){
      $("#studanswer").load(window.location.href + "#studanswer" );
}, 10000);
});

