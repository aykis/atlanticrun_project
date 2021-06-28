var h = $('.img-carre-ref').outerHeight();
$('.img-carre').css({height: h*1.1 + 'px'});
// var h1 = $('.img-carre').outerHeight();
// var w1 = $('.img-carre').outerWidth();

// // $('.overlay').css({height: h1 + 'px'});
// $('.overlay').css({width: h + 'px'});


var w = $('.slides-aigle').outerWidth();
$('.slides-aigle').css({height: w*0.80 + 'px'});

/*var w2 = $('.slides-pelican').outerWidth();*/
$('.slides-pelican').css({height: w*0.80 + 'px'});

/*var w3 = $('.slides-poulpe').outerWidth();*/
$('.slides-poulpe').css({height: w*0.80 + 'px'});

var hPic = $('.img-height-ref').outerHeight();
document.getElementById("img-height-ref").style.display = "none";
$('.cover-slides').css({height: hPic + 'px'});

(function($) {
    "use strict";

	
	$(window).on('load', function() { 
		$('.preloader').fadeOut(); 
		$('#preloader').delay(550).fadeOut('slow'); 
		$('body').delay(450).css({'overflow':'visible'});
	});
	
/* ..............................................
    Gallery
    ................................................. */
	
	$('#slides').superslides({
		inherit_width_from: '.cover-slides',
		inherit_height_from: '.cover-slides',
		play: 7000,
		animation: 'slide',
        pagination: null,
	});
	

	/* Présentation des courses */
	$('#slides-aigle').superslides({
		inherit_width_from: '.slides-aigle',
		inherit_height_from: '.slides-aigle',
		play: 7000,
		animation: 'fade',
        pagination: null,
	});
	$('#slides-pelican').superslides({
		inherit_width_from: '.slides-aigle',
		inherit_height_from: '.slides-aigle',
		play: 7000,
		animation: 'fade',
        pagination: null,
	});
	$('#slides-poulpe').superslides({
		inherit_width_from: '.slides-aigle',
		inherit_height_from: '.slides-aigle',
		play: 7000,
		animation: 'fade',
        pagination: null,
	});
	
	$( ".cover-slides ul li" ).append( "<div class='overlay-background'></div>" );
	
}(jQuery));


$('button[data-toggle="pill"]').on('hide.bs.pill', function (e) {
	var $old_tab = $($(e.target).attr("href"));
	var $new_tab = $($(e.relatedTarget).attr("href"));

	if($new_tab.index() < $old_tab.index()){
		$old_tab.css('position', 'relative').css("right", "0").show();
		$old_tab.animate({"right":"-100%"}, 300, function () {
			$old_tab.css("right", 0).removeAttr("style");
		});
	}
	else {
		$old_tab.css('position', 'relative').css("left", "0").show();
		$old_tab.animate({"left":"-100%"}, 300, function () {
			$old_tab.css("left", 0).removeAttr("style");
		});
	}
});

$('button[data-toggle="pill"]').on('show.bs.pill', function (e) {
	var $new_tab = $($(e.target).attr("href"));
	var $old_tab = $($(e.relatedTarget).attr("href"));

	if($new_tab.index() > $old_tab.index()){
		$new_tab.css('position', 'relative').css("right", "-2500px");
		$new_tab.animate({"right":"0"}, 500);
	}
	else {
		$new_tab.css('position', 'relative').css("left", "-2500px");
		$new_tab.animate({"left":"0"}, 500);
	}
});

$('button[data-toggle="pill"]').on('shown.bs.pill', function (e) {
	// your code on active tab shown
});