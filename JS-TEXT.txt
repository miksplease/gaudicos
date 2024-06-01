window.addEventListener('scroll', function() {
    var introSection = document.querySelector('.intro');
    var positionFromTop = introSection.getBoundingClientRect().top;
    var windowHeight = window.innerHeight;

    if (positionFromTop - windowHeight <= 0) {
        introSection.classList.add('show');
    }
});

window.addEventListener('scroll', function() {
    var footer = document.querySelector('.footer');

    // Calculate the scroll position
    var scrollPosition = window.scrollY || window.pageYOffset;

    // Adjust the scroll threshold as needed
    var scrollThreshold = 200; // or any other value

    if (scrollPosition > scrollThreshold) {
        footer.classList.add('show');
    } else {
        footer.classList.remove('show');
    }
});






