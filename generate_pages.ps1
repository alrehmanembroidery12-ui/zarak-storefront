$base_dir = "c:\Users\alreh\OneDrive\Desktop\my store"
$index_content = Get-Content -Raw -Path "$base_dir\index.html" -Encoding UTF8

$parts = $index_content -split '<!-- Main Content -->'
$header_part = $parts[0] + "<!-- Main Content -->`n    <main style=""margin-top: 80px;"">"

$footer_split = $parts[1] -split '</main>'
$footer_part = "    </main>`n" + $footer_split[1]

function Create-CategoryPage {
    param($filename, $title, $desc, [string[]]$imgSrcList, [switch]$isSale)

    $products_html = @"
        <section class="section products-section">
            <div class="container">
                <div class="section-title">
                    <h2 style="font-size: 3rem; margin-top: 20px;">$title</h2>
                    <p>$desc</p>
                </div>
                <div class="product-grid" style="margin-top: 40px;">
"@

    for ($i = 0; $i -lt 8; $i++) {
        $img_src = $imgSrcList[$i % $imgSrcList.Length]
        $price = "Rs. " + (4000 + ($i * 1000)) + ",999"
        $sale_badge = ""
        $orig_price = ""
        
        if ($isSale -or ($i % 3 -eq 0)) {
            $sale_badge = '<span class="discount-badge">-20%</span>'
            $orig_price = '<span class="original-price">Rs. ' + (5000 + ($i * 1500)) + ',999</span>'
        }

        $i_plus_1 = $i + 1
        $products_html += @"
                    <div class="product-card">
                        <div class="product-image">
                            $sale_badge
                            <a href="product.html" style="display:block; height:100%;">
                                <img src="$img_src" alt="Premium Product $i_plus_1">
                            </a>
                            <button class="quick-add-btn">Add to Cart</button>
                        </div>
                        <div class="product-info">
                            <div class="product-rating">
                                <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star-half-alt"></i>
                                <span>(12$i)</span>
                            </div>
                            <h3 class="product-title">Premium ZĀRAK Item $i_plus_1</h3>
                            <div class="product-price">
                                <span class="current-price">$price</span>
                                $orig_price
                            </div>
                        </div>
                    </div>
"@
    }

    $products_html += @"
                </div>
            </div>
        </section>
"@

    $full_html = $header_part.Replace("<title>ZĀRAK", "<title>$title | ZĀRAK") + $products_html + $footer_part
    Set-Content -Path "$base_dir\$filename" -Value $full_html -Encoding UTF8
}

function Create-TextPage {
    param($filename, $title, $content_html)
    
    $text_html = @"
        <section class="section" style="padding-top: 120px; padding-bottom: 80px; min-height: 60vh;">
            <div class="container" style="max-width: 800px; margin: 0 auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
                <h1 style="font-size: 2.5rem; margin-bottom: 20px; color: var(--color-primary); border-bottom: 2px solid var(--color-accent); padding-bottom: 15px;">$title</h1>
                <div style="color: var(--color-text-light); line-height: 1.8; font-size: 1.05rem;">
                    $content_html
                </div>
            </div>
        </section>
"@
    $full_html = $header_part.Replace("<title>ZĀRAK", "<title>$title | ZĀRAK") + $text_html + $footer_part
    Set-Content -Path "$base_dir\$filename" -Value $full_html -Encoding UTF8
}

[string[]]$images = @("images/perfume_bottle.png", "images/silk_dress.png", "images/mens_wallet.png", "images/home_decor_vase.png")

Create-CategoryPage "new-in.html" "New Arrivals" "Discover the latest additions to our premium collection." $images
Create-CategoryPage "fashion.html" "Premium Fashion" "Elevate your wardrobe with our latest high-end apparel." @("images/silk_dress.png", "images/mens_wallet.png")
Create-CategoryPage "beauty.html" "Beauty & Fragrance" "Luxurious scents and beauty essentials for the modern lifestyle." @("images/perfume_bottle.png")
Create-CategoryPage "living.html" "Home Decor" "Minimalist, sophisticated pieces to transform your living space." @("images/home_decor_vase.png")
Create-CategoryPage "sale.html" "Flash Sale" "Exclusive discounts on our finest ZĀRAK select pieces." $images -isSale
Create-CategoryPage "collection.html" "Our Complete Collection" "Explore the full range of ZĀRAK premium lifestyle products." $images

$lorem = "<p style='margin-bottom: 15px;'>This is a dummy page created to showcase the premium layout. In a real production environment, this section would contain detailed policies tailored for Pakistani customers.</p>" * 3

Create-TextPage "secure-payment.html" "Secure Payments & Cash on Delivery" ("<h3>Payment Options</h3><p>We are proud to offer Nationwide Cash on Delivery (COD) across Pakistan. You can also pay securely using JazzCash, EasyPaisa, or direct Bank Transfer. Your transactions are 100% secure.</p>" + $lorem)

Create-TextPage "returns.html" "7-Day Easy Returns" ("<h3>Our Return Policy</h3><p>If you are not entirely satisfied with your premium ZĀRAK purchase, we're here to help. You have 7 calendar days to return an item from the date you received it.</p>" + $lorem)

Create-TextPage "shipping.html" "Nationwide Shipping" ("<h3>Delivery Information</h3><p>We deliver to all major cities in Pakistan within 3-5 working days. Enjoy free shipping on all orders above Rs. 5,000.</p>" + $lorem)

Create-TextPage "faq.html" "Frequently Asked Questions" ("<h3>Have a Question?</h3><p>Find answers to our most commonly asked questions below regarding orders, shipping, and authentic ZĀRAK products.</p>" + $lorem)

Create-TextPage "track.html" "Track Your Order" ("<h3>Order Tracking</h3><p>Please enter your order ID and the email address used during checkout to track the status of your delivery.</p><br><input type='text' placeholder='Order ID' style='padding: 10px; width: 100%; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;'><button class='btn btn-primary'>Track Order</button>")

Create-TextPage "contact.html" "Contact Us" ("<h3>Get in Touch</h3><p>Our premium support team is available 24/7. Reach out to us via WhatsApp for instant assistance.</p><br><a href='#' class='btn btn-primary' style='background-color: #25D366; border:none;'><i class='fab fa-whatsapp'></i> Chat on WhatsApp</a>")

Create-TextPage "privacy.html" "Privacy Policy" ("<h3>Your Privacy</h3><p>ZĀRAK is committed to protecting your privacy. This policy outlines how we collect, use, and safeguard your personal information.</p>" + $lorem)

Create-TextPage "terms.html" "Terms of Service" ("<h3>Terms & Conditions</h3><p>By accessing or using the ZĀRAK website, you agree to be bound by these terms of service and all applicable laws and regulations.</p>" + $lorem)

Write-Host "Successfully generated all 14 pages!"
