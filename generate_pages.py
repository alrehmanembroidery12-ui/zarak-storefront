import os

base_dir = os.path.dirname(os.path.abspath(__file__))

# Curated premium product database for ZARAK
fashion_products = [
    {
        "title": "ZĀRAK Amber Silk Anarkali",
        "price": "Rs. 14,999",
        "orig_price": "Rs. 18,999",
        "img": "https://images.unsplash.com/photo-1609357605129-26f69add5d6e?auto=format&fit=crop&w=600&q=80",
        "rating": "4.9",
        "reviews": "145"
    },
    {
        "title": "Emerald Velvet Shawl",
        "price": "Rs. 8,999",
        "orig_price": "Rs. 11,499",
        "img": "https://images.unsplash.com/photo-1608748010899-18f300247112?auto=format&fit=crop&w=600&q=80",
        "rating": "4.8",
        "reviews": "92"
    },
    {
        "title": "Royal Ivory Sherwani",
        "price": "Rs. 24,999",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1621184455862-c163dfb30e0f?auto=format&fit=crop&w=600&q=80",
        "rating": "5.0",
        "reviews": "34"
    },
    {
        "title": "Peshawari Leather Chappal",
        "price": "Rs. 5,999",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1605812860427-4024433a70fd?auto=format&fit=crop&w=600&q=80",
        "rating": "4.7",
        "reviews": "108"
    },
    {
        "title": "Chic Leather Shoulder Bag",
        "price": "Rs. 9,499",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?auto=format&fit=crop&w=600&q=80",
        "rating": "4.6",
        "reviews": "76"
    },
    {
        "title": "Classic Linen Kurta",
        "price": "Rs. 4,499",
        "orig_price": "Rs. 5,999",
        "img": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=600&q=80",
        "rating": "4.5",
        "reviews": "180"
    },
    {
        "title": "Premium Leather Wallet",
        "price": "Rs. 3,499",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1627123424574-724758594e93?auto=format&fit=crop&w=600&q=80",
        "rating": "4.8",
        "reviews": "230"
    },
    {
        "title": "Tan Leather Loafers",
        "price": "Rs. 7,999",
        "orig_price": "Rs. 9,999",
        "img": "https://images.unsplash.com/photo-1533867617858-e7b97e060509?auto=format&fit=crop&w=600&q=80",
        "rating": "4.9",
        "reviews": "64"
    }
]

beauty_products = [
    {
        "title": "Royal Oud Intense Perfume",
        "price": "Rs. 12,499",
        "orig_price": "Rs. 15,999",
        "img": "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=600&q=80",
        "rating": "4.9",
        "reviews": "312"
    },
    {
        "title": "Kashmiri Rose Facial Serum",
        "price": "Rs. 3,899",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?auto=format&fit=crop&w=600&q=80",
        "rating": "4.8",
        "reviews": "154"
    },
    {
        "title": "Amber Musk Eau De Parfum",
        "price": "Rs. 9,999",
        "orig_price": "Rs. 12,499",
        "img": "https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=600&q=80",
        "rating": "4.9",
        "reviews": "88"
    },
    {
        "title": "Matte Lip Crayon Set",
        "price": "Rs. 4,499",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=600&q=80",
        "rating": "4.6",
        "reviews": "112"
    },
    {
        "title": "Organic Face Radiance Cream",
        "price": "Rs. 2,999",
        "orig_price": "Rs. 3,999",
        "img": "https://images.unsplash.com/photo-1601049541289-9b1b7bbbfe19?auto=format&fit=crop&w=600&q=80",
        "rating": "4.5",
        "reviews": "95"
    },
    {
        "title": "Luxury Oud Body Wash",
        "price": "Rs. 1,899",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=600&q=80",
        "rating": "4.7",
        "reviews": "241"
    },
    {
        "title": "Pure Argan Hair Elixir",
        "price": "Rs. 4,299",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1617897903246-719242758050?auto=format&fit=crop&w=600&q=80",
        "rating": "4.8",
        "reviews": "167"
    },
    {
        "title": "Gold Radiance Face Serum",
        "price": "Rs. 5,499",
        "orig_price": "Rs. 6,999",
        "img": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=600&q=80",
        "rating": "5.0",
        "reviews": "45"
    }
]

living_products = [
    {
        "title": "Antique Brass Incense Holder",
        "price": "Rs. 3,499",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1603006905003-be475563bc59?auto=format&fit=crop&w=600&q=80",
        "rating": "4.7",
        "reviews": "54"
    },
    {
        "title": "Embroidered Linen Cushion Cover",
        "price": "Rs. 2,299",
        "orig_price": "Rs. 2,999",
        "img": "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?auto=format&fit=crop&w=600&q=80",
        "rating": "4.8",
        "reviews": "132"
    },
    {
        "title": "Polished Hexagonal Marble Coasters",
        "price": "Rs. 1,899",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1618220179428-22790b461013?auto=format&fit=crop&w=600&q=80",
        "rating": "4.9",
        "reviews": "210"
    },
    {
        "title": "Hand-thrown Terracotta Plant Pot",
        "price": "Rs. 1,499",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?auto=format&fit=crop&w=600&q=80",
        "rating": "4.6",
        "reviews": "78"
    },
    {
        "title": "Minimalist Matte Black Table Lamp",
        "price": "Rs. 6,999",
        "orig_price": "Rs. 8,499",
        "img": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=600&q=80",
        "rating": "4.8",
        "reviews": "41"
    },
    {
        "title": "Glazed Ceramic Serving Bowl",
        "price": "Rs. 2,899",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1612196808214-b8e1d6145a8c?auto=format&fit=crop&w=600&q=80",
        "rating": "4.7",
        "reviews": "165"
    },
    {
        "title": "Hand-carved Teakwood Serving Tray",
        "price": "Rs. 4,499",
        "orig_price": "",
        "img": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=600&q=80",
        "rating": "4.8",
        "reviews": "83"
    },
    {
        "title": "Scented Amber Soy Wax Candle",
        "price": "Rs. 1,799",
        "orig_price": "Rs. 2,499",
        "img": "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=600&q=80",
        "rating": "4.9",
        "reviews": "119"
    }
]

# Create combinations for mixed pages
new_in_products = [
    fashion_products[0], fashion_products[1], fashion_products[2],
    beauty_products[0], beauty_products[1], beauty_products[2],
    living_products[0], living_products[1]
]

# Sale products (those with orig_price configured)
sale_products = [p for p in fashion_products + beauty_products + living_products if p["orig_price"]][:8]

# Complete catalog mix
collection_products = [
    fashion_products[0], fashion_products[3], fashion_products[4],
    beauty_products[0], beauty_products[4], beauty_products[5],
    living_products[1], living_products[4]
]

def generate_pages():
    with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
        content = f.read()
    
    # Split index.html into header and footer parts and inject premium overrides CSS link
    raw_header = content.split("<!-- Main Content -->")[0]
    header_part = raw_header + "<!-- Main Content -->\n    <main style=\"margin-top: 0px;\">"
    footer_part = "    </main>\n" + content.split("</main>")[1]
    
    # Helper for generating category pages
    def create_category_page(filename, title, desc, product_list, hero_img):
        products_html = f"""
        <!-- Category Hero Banner -->
        <section class="category-hero" style="background-image: url('{hero_img}');">
            <div class="category-hero-content">
                <span class="category-tag">ZĀRAK SELECT</span>
                <h1>{title}</h1>
                <p>{desc}</p>
                <div class="hero-scroll-indicator">
                    <span class="mouse-scroll"></span>
                </div>
            </div>
        </section>

        <section class="section products-section reveal-on-scroll" style="padding-top: 80px; padding-bottom: 120px;">
            <div class="container">
                <div class="product-grid">
        """
        
        for idx, p in enumerate(product_list):
            img_src = p["img"]
            name = p["title"]
            price = p["price"]
            orig = p["orig_price"]
            rating = p["rating"]
            reviews = p["reviews"]
            
            discount = ""
            orig_html = ""
            if orig:
                discount = '<span class="discount-badge">-20%</span>'
                orig_html = f'<span class="original-price">{orig}</span>'
            
            # Simple star builder
            stars_html = ""
            full_stars = int(float(rating))
            for _ in range(full_stars):
                stars_html += '<i class="fas fa-star"></i>'
            if float(rating) % 1 != 0:
                stars_html += '<i class="fas fa-star-half-alt"></i>'
            
            products_html += f"""
                    <div class="product-card">
                        <div class="product-image">
                            {discount}
                            <a href="product.html" style="display:block; height:100%;">
                                <img src="{img_src}" alt="{name}">
                            </a>
                            <button class="quick-add-btn">Add to Cart</button>
                        </div>
                        <div class="product-info">
                            <div class="product-rating">
                                {stars_html}
                                <span>({reviews})</span>
                            </div>
                            <h3 class="product-title">{name}</h3>
                            <div class="product-price">
                                <span class="current-price">{price}</span>
                                {orig_html}
                            </div>
                        </div>
                    </div>
            """
            
        products_html += """
                </div>
            </div>
        </section>
        """
        
        full_html = header_part.replace("<title>ZĀRAK", f"<title>{title} | ZĀRAK") + products_html + footer_part
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
            f.write(full_html)
            
    # Helper for generating text/policy pages
    def create_text_page(filename, title, content_html):
        text_html = f"""
        <section class="section" style="padding-top: 120px; padding-bottom: 80px; min-height: 60vh;">
            <div class="container" style="max-width: 800px; margin: 0 auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
                <h1 style="font-size: 2.5rem; margin-bottom: 20px; color: var(--color-primary); border-bottom: 2px solid var(--color-accent); padding-bottom: 15px;">{title}</h1>
                <div style="color: var(--color-text-light); line-height: 1.8; font-size: 1.05rem;">
                    {content_html}
                </div>
            </div>
        </section>
        """
        full_html = header_part.replace("<title>ZĀRAK", f"<title>{title} | ZĀRAK") + text_html + footer_part
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
            f.write(full_html)
 
    # 1. Generate Category Pages with unique data and Hero Banners
    create_category_page("new-in.html", "New Arrivals", "Discover the latest additions to our premium collection.", new_in_products, "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=1600&q=80")
    create_category_page("fashion.html", "Premium Fashion", "Elevate your wardrobe with our latest high-end apparel.", fashion_products, "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=1600&q=80")
    create_category_page("beauty.html", "Beauty & Fragrance", "Luxurious scents and beauty essentials for the modern lifestyle.", beauty_products, "https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=1600&q=80")
    create_category_page("living.html", "Home Decor", "Minimalist, sophisticated pieces to transform your living space.", living_products, "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=1600&q=80")
    create_category_page("sale.html", "Flash Sale", "Exclusive discounts on our finest ZĀRAK select pieces.", sale_products, "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=1600&q=80")
    create_category_page("collection.html", "Our Complete Collection", "Explore the full range of ZĀRAK premium lifestyle products.", collection_products, "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=1600&q=80")
    
    # 2. Generate Policy / Info Pages
    lorem = "<p style='margin-bottom: 15px;'>This is a dummy page created to showcase the premium layout. In a real production environment, this section would contain detailed policies tailored for Pakistani customers.</p>" * 3
    
    create_text_page("secure-payment.html", "Secure Payments & Cash on Delivery", 
                     "<h3>Payment Options</h3><p>We are proud to offer Nationwide Cash on Delivery (COD) across Pakistan. You can also pay securely using JazzCash, EasyPaisa, or direct Bank Transfer. Your transactions are 100% secure.</p>" + lorem)
    
    create_text_page("returns.html", "7-Day Easy Returns", 
                     "<h3>Our Return Policy</h3><p>If you are not entirely satisfied with your premium ZĀRAK purchase, we're here to help. You have 7 calendar days to return an item from the date you received it.</p>" + lorem)
                      
    create_text_page("shipping.html", "Nationwide Shipping", 
                     "<h3>Delivery Information</h3><p>We deliver to all major cities in Pakistan within 3-5 working days. Enjoy free shipping on all orders above Rs. 5,000.</p>" + lorem)
                      
    create_text_page("faq.html", "Frequently Asked Questions", 
                     "<h3>Have a Question?</h3><p>Find answers to our most commonly asked questions below regarding orders, shipping, and authentic ZĀRAK products.</p>" + lorem)
                      
    create_text_page("track.html", "Track Your Order", 
                     "<h3>Order Tracking</h3><p>Please enter your order ID and the email address used during checkout to track the status of your delivery.</p><br><input type='text' placeholder='Order ID' style='padding: 10px; width: 100%; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;'><button class='btn btn-primary'>Track Order</button>")
                      
    create_text_page("contact.html", "Contact Us", 
                     "<h3>Get in Touch</h3><p>Our premium support team is available 24/7. Reach out to us via WhatsApp for instant assistance.</p><br><a href='#' class='btn btn-primary' style='background-color: #25D366; border:none;'><i class='fab fa-whatsapp'></i> Chat on WhatsApp</a>")
                      
    create_text_page("privacy.html", "Privacy Policy", 
                     "<h3>Your Privacy</h3><p>ZĀRAK is committed to protecting your privacy. This policy outlines how we collect, use, and safeguard your personal information.</p>" + lorem)
                      
    create_text_page("terms.html", "Terms of Service", 
                     "<h3>Terms & Conditions</h3><p>By accessing or using the ZĀRAK website, you agree to be bound by these terms of service and all applicable laws and regulations.</p>" + lorem)
                      
    print("Successfully generated all 14 pages with premium category hero sections and CSS overrides!")

if __name__ == "__main__":
    generate_pages()
