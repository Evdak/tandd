document.addEventListener("DOMContentLoaded", function (event) {
    setInterval(() => {
        document.querySelectorAll('.select2-selection__choice__display').forEach(el => {
            if (el.textContent.includes('<img')) {
                el.innerHTML = el.textContent;
            }
        });

        document.querySelectorAll('.select2-selection__rendered').forEach(el => {
            if (el.textContent.includes('<img')) {
                el.innerHTML = el.textContent;
            }
        });

        document.querySelectorAll('.select2-results__option.select2-results__option--selectable').forEach(el => {
            if (el.textContent.includes('<img')) {
                el.innerHTML = el.textContent;
            }
        });

        document.querySelectorAll('.select2-selection.select2-selection--single').forEach(el => {
            el.style.height = 'auto';
        })
    }, 1000);
});