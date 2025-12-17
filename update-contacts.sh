#!/bin/bash

# This script updates all contact details in index.html

echo "🔄 Updating all contact details..."

# Create a temporary file
cp index.html index.html.tmp

# 1. Update Instagram URL in schema (line 100)
sed -i 's|"https://www.instagram.com/butterflybloom.cdc"|"https://www.instagram.com/butterflybloom_cdc/"|g' index.html.tmp

# 2. Update phone in schema (line 66)
sed -i 's|"telephone": "+919876543210"|"telephone": "+918019589810"|g' index.html.tmp

# 3. Update email in schema (line 67)
sed -i 's|"email": "info@butterflybloomcdc.com"|"email": "hello@butterflybloomcdc.com"|g' index.html.tmp

# 4. Update address in schema (lines 68-72)
sed -i 's|"addressLocality": "Visakhapatnam",|"streetAddress": "2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony",\n        "addressLocality": "Visakhapatnam",\n        "postalCode": "530017",|g' index.html.tmp

# 5. Update closing time in schema (line 85)
sed -i 's|"closes": "18:00"|"closes": "19:00"|g' index.html.tmp

# 6. Update "Team trained" to "Team served" (line 1311)
sed -i 's|Team trained in USA, UK, and across India|Team served to USA, UK, and across India|g' index.html.tmp

# 7. Update location in contact section (line 1467)
sed -i 's|<p>Visakhapatnam<br>Andhra Pradesh, India</p>|<p>2nd Floor, Door No: 1, 53-8/2<br>Sector 1, MVP Colony<br>Visakhapatnam, AP 530017</p>|g' index.html.tmp

# 8. Update phone in contact section (line 1472)
sed -i 's|<a href="tel:+919876543210">+91 98765 43210</a>|<a href="tel:+918019589810">+91 80195 89810</a>|g' index.html.tmp

# 9. Update email in contact section (line 1477)
sed -i 's|<a href="mailto:info@butterflybloomcdc.com">info@butterflybloomcdc.com</a>|<a href="mailto:hello@butterflybloomcdc.com">hello@butterflybloomcdc.com</a>|g' index.html.tmp

# 10. Update hours in contact section (line 1482)
sed -i 's|<p>Mon - Sat: 9:00 AM - 6:00 PM<br>Sunday: By Appointment</p>|<p>Mon - Sat: 9:00 AM - 7:00 PM<br>Sunday: By Appointment<br><strong>📅 On Appointment Basis Only</strong><br>Limited slots per week</p>|g' index.html.tmp

# 11. Update WhatsApp link (line 1487)
sed -i 's|<a href="https://wa.me/919876543210"|<a href="https://wa.me/918019589810"|g' index.html.tmp

# 12. Update Instagram in contact section (line 1492)
sed -i 's|<a href="https://www.instagram.com/butterflybloom.cdc" target="_blank">@butterflybloom.cdc</a>|<a href="https://www.instagram.com/butterflybloom_cdc/" target="_blank">@butterflybloom_cdc</a>|g' index.html.tmp

# 13. Update Instagram in footer (line 1509)
sed -i 's|<a href="https://www.instagram.com/butterflybloom.cdc" target="_blank">Instagram</a>|<a href="https://www.instagram.com/butterflybloom_cdc/" target="_blank">Instagram</a>|g' index.html.tmp

# Replace original file
mv index.html.tmp index.html

echo "✅ All contact details updated successfully!"
echo ""
echo "Updated details:"
echo "- Instagram: https://www.instagram.com/butterflybloom_cdc/ (@butterflybloom_cdc)"
echo "- Phone: +91-8019589810"
echo "- Email: hello@butterflybloomcdc.com"
echo "- Location: 2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony, Visakhapatnam, AP 530017"
echo "- Hours: Mon-Sat 9 AM - 7 PM (On appointment basis only)"
