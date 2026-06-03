document.addEventListener("DOMContentLoaded", function () {
  // --- 1. Scrolled Header Transition ---
  const header = document.querySelector(".header");

  function checkScroll() {
    if (window.scrollY > 50) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }
  }

  // Initial check in case page starts scrolled down
  checkScroll();
  window.addEventListener("scroll", checkScroll);

  // --- 2. Intersection Observer for Scroll Reveals ---
  const revealElements = document.querySelectorAll(".reveal-on-scroll");

  if ("IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("active");
            // Stop observing once animated for performance and clean feel
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.1,
        rootMargin: "0px 0px -60px 0px", // Trigger slightly before entering fully
      }
    );

    revealElements.forEach((el) => {
      revealObserver.observe(el);
    });
  } else {
    // Fallback if IntersectionObserver is not supported
    revealElements.forEach((el) => {
      el.classList.add("active");
    });
  }

  // --- 3. Smooth Slideshow Autoplay ---
  const slides = document.querySelectorAll(".slideshow-container .slide");
  let currentSlide = 0;

  if (slides.length > 1) {
    setInterval(() => {
      slides[currentSlide].classList.remove("active");
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add("active");
    }, 4500); // Rotate every 4.5 seconds
  }
});
