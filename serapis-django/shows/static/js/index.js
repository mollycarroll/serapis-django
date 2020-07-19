// JS to add links to mobile burger menu
document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach(el => {
      el.addEventListener('click', () => {

        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById('SerapisNav');

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

      });
    });
  }

});

// photo slider
var slideIndex = 0;

function serapiSlides(s) {
  var arrSlides = [...s];
  var i;
  for (i = 0; i < arrSlides.length; i++) {
    s[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > arrSlides.length) {
    slideIndex = 1;
  }
  arrSlides[slideIndex - 1].style.display = "block";
  setTimeout(serapiSlides, 10000);

  console.log('serapiSlides is live');
}