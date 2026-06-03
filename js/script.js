document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
            navLinks.style.flexDirection = 'column';
            navLinks.style.position = 'absolute';
            navLinks.style.top = '80px';
            navLinks.style.left = '0';
            navLinks.style.width = '100%';
            navLinks.style.backgroundColor = 'rgba(255,255,255,0.98)';
            navLinks.style.padding = '20px';
            navLinks.style.boxShadow = '0 10px 15px rgba(0,0,0,0.05)';
        });
    }

    // 2. Dummy Cart Functionality
    const cartCountElements = document.querySelectorAll('.cart-count');
    const addToCartBtns = document.querySelectorAll('.quick-add-btn, .btn-outline');
    let cartCount = 0;

    addToCartBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            cartCount++;
            cartCountElements.forEach(el => {
                el.textContent = cartCount;
                // Add pop animation
                el.style.transform = 'scale(1.5)';
                el.style.transition = 'transform 0.2s ease';
                setTimeout(() => {
                    el.style.transform = 'scale(1)';
                }, 200);
            });

            // Optional: change button text temporarily
            const originalText = btn.textContent;
            btn.textContent = 'Added!';
            btn.style.backgroundColor = 'var(--color-primary)';
            btn.style.color = 'white';
            setTimeout(() => {
                btn.textContent = originalText;
                btn.style.backgroundColor = '';
                btn.style.color = '';
            }, 1000);
        });
    });

    // 3. Countdown Timer (Flash Sale)
    const countdownEl = document.getElementById('countdown');
    if (countdownEl) {
        // Set date to 2 days from now for dummy effect
        const countDownDate = new Date().getTime() + (2 * 24 * 60 * 60 * 1000) + (14 * 60 * 60 * 1000) + (35 * 60 * 1000);

        setInterval(function () {
            const now = new Date().getTime();
            const distance = countDownDate - now;

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            document.getElementById('days').textContent = days.toString().padStart(2, '0');
            document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
            document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
            document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
        }, 1000);
    }

    // 4. Product Gallery Thumbnail Switching & Zoom
    const thumbnails = document.querySelectorAll('.thumbnail');
    const mainImg = document.getElementById('main-product-img');

    if (thumbnails.length > 0 && mainImg) {
        thumbnails.forEach(thumb => {
            thumb.addEventListener('click', function () {
                // Remove active class from all
                thumbnails.forEach(t => t.classList.remove('active'));
                // Add to clicked
                this.classList.add('active');

                // If it has an image inside, swap main image
                const img = this.querySelector('img');
                if (img) {
                    mainImg.style.transition = 'opacity 0.2s';
                    mainImg.style.opacity = 0;
                    setTimeout(() => {
                        mainImg.src = img.src;
                        mainImg.style.opacity = 1;
                    }, 200);
                }
            });
        });

        // Basic inner zoom effect on main image hover
        const mainImageContainer = document.querySelector('.main-image');
        mainImageContainer.addEventListener('mousemove', function (e) {
            const { left, top, width, height } = this.getBoundingClientRect();
            const x = (e.clientX - left) / width * 100;
            const y = (e.clientY - top) / height * 100;

            mainImg.style.transition = 'transform 0.1s ease';
            mainImg.style.transformOrigin = `${x}% ${y}%`;
            mainImg.style.transform = 'scale(1.8)';
        });

        mainImageContainer.addEventListener('mouseleave', function () {
            mainImg.style.transition = 'transform 0.3s ease';
            mainImg.style.transformOrigin = 'center';
            mainImg.style.transform = 'scale(1)';
        });
    }

    // 5. FAQ Accordion
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    accordionHeaders.forEach(header => {
        header.addEventListener('click', function () {
            const content = this.nextElementSibling;
            const icon = this.querySelector('i');

            if (content.style.display === 'block') {
                content.style.display = 'none';
                icon.className = 'fas fa-chevron-down';
            } else {
                // Close others
                document.querySelectorAll('.accordion-content').forEach(c => c.style.display = 'none');
                document.querySelectorAll('.accordion-header i').forEach(i => i.className = 'fas fa-chevron-down');

                content.style.display = 'block';
                icon.className = 'fas fa-chevron-up';
            }
        });
    });
});
