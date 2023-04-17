jQuery(document).ready(function ($) {
    "use strict";
    $('.owl-carousel').owlCarousel({
        margin: 10,
        // loop: true,
        // autoWidth: true,
        dots: true,
        autoHeight: true,
        items: 2,
        // animateOut: 'fadeOut',
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            1170: {
                items: 3
            }
        },
    })
});