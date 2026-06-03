document.addEventListener("DOMContentLoaded", function() {
    // --- 1. Store Settings (Naam aur Hero Banner) ---
    const savedSettings = localStorage.getItem('storeSettings');
    if(savedSettings) {
        const settings = JSON.parse(savedSettings);

        if (settings.storeName && settings.storeName.trim() !== "") {
            const logos = document.querySelectorAll('.logo');
            logos.forEach(logo => logo.textContent = settings.storeName);
        }

        const heroTitle = document.querySelector('.hero-content h1');
        const heroDesc = document.querySelector('.hero-content p');
        const heroImg = document.getElementById('hero-img');

        if(heroTitle && settings.heroTitle && settings.heroTitle.trim() !== "") { heroTitle.innerHTML = settings.heroTitle; }
        if(heroDesc && settings.heroDesc && settings.heroDesc.trim() !== "") { heroDesc.textContent = settings.heroDesc; }
        if(heroImg && settings.heroImg && settings.heroImg.trim() !== "") { heroImg.src = settings.heroImg; }
    }

    // --- 2. Dynamic Categories ---
    const savedCategories = localStorage.getItem('storeCategories');
    const categoryGrid = document.getElementById('dynamic-category-grid');
    if(savedCategories && categoryGrid) {
        const categories = JSON.parse(savedCategories);
        categoryGrid.innerHTML = ''; 
        categories.forEach(cat => {
            categoryGrid.innerHTML += `
                <a href="${cat.link}" class="category-card">
                    <img src="${cat.image}" alt="${cat.name}">
                    <div class="category-content">
                        <h3>${cat.name}</h3>
                        <span>Explore</span>
                    </div>
                </a>
            `;
        });
    }

    // --- 3. Dynamic Products (WITH SMART FILTER) ---
    const savedProducts = localStorage.getItem('storeProducts');
    const productGrid = document.getElementById('dynamic-product-grid');

    if (savedProducts && productGrid) {
        let products = JSON.parse(savedProducts);
        
        // Browser ko pata chalega ke konsa page open hai
        const currentPage = window.location.pathname.toLowerCase();
        
        // Smart Filter Logic
        if (currentPage.includes('fashion.html')) {
            products = products.filter(prod => prod.category === 'Fashion');
        } else if (currentPage.includes('beauty.html')) {
            products = products.filter(prod => prod.category === 'Beauty');
        } else if (currentPage.includes('living.html')) {
            products = products.filter(prod => prod.category === 'Home Decor');
        } 
        // Agar new-in, collection ya main page hai toh saari products show hongi

        productGrid.innerHTML = ''; // Purana kachra saaf karein

        // Agar us category mein koi product nahi hai
        if (products.length === 0) {
            productGrid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; font-size: 1.2rem; color: gray; padding: 50px 0;">No products added in this category yet. Add from Admin Panel.</p>';
        } else {
            // Nayi filtered products lagayen
            products.forEach(prod => {
                productGrid.innerHTML += `
                    <div class="product-card">
                        <div class="product-image">
                            <a href="#" style="display:block; height:100%;">
                                <img src="${prod.image}" alt="${prod.name}">
                            </a>
                            <button class="quick-add-btn">Add to Cart</button>
                        </div>
                        <div class="product-info">
                            <div class="product-rating">
                                <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star-half-alt"></i>
                            </div>
                            <h3 class="product-title">${prod.name}</h3>
                            <div class="product-price">
                                <span class="current-price">${prod.price}</span>
                                <span style="font-size: 0.8rem; color: #94a3b8; display: block; margin-top: 5px;">Category: ${prod.category}</span>
                            </div>
                        </div>
                    </div>
                `;
            });
        }
    }
});