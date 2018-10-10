$(document).ready(function() {

    // vertical alignment of search bar and Suggest button inside navigation bar
    $(".menu-search").css("padding-top", ($(".menu-search").height() - $("#custom-search-input").height()) / 2);
    $(".menu-contact-link").css("padding-top", ($(".menu-contact-link").height() - $(".menu-contact-link a").height()) / 2);

    // bx-slider on header
    $(".slider").bxSlider({
        mode: 'fade',
        controls: false,
        pager: false,
        responsive: true,
        touchEnabled: true,
        auto: true,
        autoStart: true,
        margin: 0,
        speed: '1000'
    });

    $("iframe").height($("iframe").width() * 0.6);

});
