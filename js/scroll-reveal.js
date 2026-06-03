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

  // --- 3. Subtle Parallax for Hero Image ---
  const heroImage = document.querySelector(".hero-image img");
  if (heroImage) {
    window.addEventListener("scroll", function () {
      const scrollPosition = window.pageYOffset;
      // Move background image slower than content
      heroImage.style.transform = `scale(1.08) translateY(${scrollPosition * 0.15}px)`;
    });
  }
});
