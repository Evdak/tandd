document.addEventListener('DOMContentLoaded', function () { // Аналог $(document).ready(function(){
    // const buttonLeft = document.getElementById('offer-pagination-left');
    // const buttonRight = document.getElementById('offer-pagination-right');
    // const offerSlider = document.getElementById('offers-slider');

    // buttonRight.onclick = function () {
    //     card = offerSlider.querySelector('.card');
    //     col = card.closest('.col');
    //     scrollValue = col.scrollWidth;
    //     console.log(scrollValue);
    //     offerSlider.scrollLeft += scrollValue;
    // };
    // buttonLeft.onclick = function () {
    //     card = offerSlider.querySelector('.card');
    //     col = card.closest('.col');
    //     scrollValue = col.scrollWidth;
    //     console.log(scrollValue);
    //     offerSlider.scrollLeft -= scrollValue;
    // };

    $("#phone2").mask("+7 (999) 999-99-99");
    $("#phone-1").mask("+7 (999) 999-99-99");
});


