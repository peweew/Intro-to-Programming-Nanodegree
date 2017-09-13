$(document).ready(function(){         
    /*input form effect*/
    $("input").focus(function(){
        $(this).css("background-color", "#F1F1F1");
    });
    $("input").blur(function(){
        $(this).css("background-color", "#ffffff");
    });
    $("textarea").focus(function(){
        $(this).css("background-color", "#F1F1F1");
    });
    $("textarea").blur(function(){
        $(this).css("background-color", "#ffffff");
    });
    /*slide down menu*/
	$("#nav_home").hover(function(){
        $("#nav_home_sub").stop().slideToggle("fast");
    }); 
    $("#nav_member").hover(function(){
        $("#nav_member_sub").stop().slideToggle("fast");        
    }); 
    $("#nav_photo").hover(function(){
        $("#nav_photo_sub").stop().slideToggle("fast");         
    }); 
});

 