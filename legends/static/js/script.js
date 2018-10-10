$(document).ready(function() {

    $('.slider').bxSlider({
        mode: 'fade',
        infiniteLoop: true,
        responsive: true,
        touchEnabled: true,
        auto: true,
        autoStart: true,
        controls: false,
        margin: 0,
        pager: false
    });

    $(".popular").bxSlider({
        mode: 'horizontal',
        infiniteLoop: true,
        responsive: true,
        touchEnabled: true,
        auto: true,
        autoStart: true,
        controls: false,
        adaptiveHeight: false,
        pager: false
    });


    $(".menu-button-container").css("padding-left", $(".container").css("margin-left"));
    $(".menu-button-container").css("padding-right", $(".container").css("margin-right"));
    $(".article-header-parent").height($(".article-header-parent").width());

    $(".menu-search").css("padding-top", ($(".menu-search").height() - $("#custom-search-input").height()) / 2);
    $(".menu-contact-link").css("padding-top", ($(".menu-contact-link").height() - $(".menu-contact-link a").height()) / 2);
    //$(".article-footer").height($(".article-header").height()/5);
    $(".menu-button").click(function() {
        if($(window).width() < 576) {
            $(".menu-container").animate({width: '100%'}, "100");
        } else if ($(window).width() > 575 && $(window).width() < 768) {
            $(".menu-container").animate({width: '40%'}, "100");
        } else {
            $(".menu-container").animate({width: '30%'}, "100");
        }
        $(".menu-close").show();
        $(".menu-container").css("padding","50");

        $(".menu-close").click(function() {
            $(".menu-close").hide();
            $(".menu-container").css("padding","0");
            $(".menu-container").animate({width: '0'}, "300");
        })
    });
    $(".popular-overlay").height($(".popular-container img").height());
    $(".popular-overlay").width($(".popular-container img").width());
    $(".popular-container").mouseenter(function () {
        $(this).find(".popular-overlay").fadeIn(300);
    });
    $(".popular-container").mouseleave(function () {
        $(this).find(".popular-overlay").fadeOut(300);
    });
});
