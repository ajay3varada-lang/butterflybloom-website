#!/usr/bin/env python3
"""
Update all contact details in the Butterfly Bloom CDC website
"""

import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Starting updates...")

# 1. Update Instagram handle (URL and display text)
html = html.replace('https://www.instagram.com/butterflybloom.cdc', 'https://www.instagram.com/butterflybloom_cdc')
html = html.replace('@butterflybloom.cdc', '@butterflybloom_cdc')
print("✓ Instagram handle updated")

# 2. Update phone numbers (all formats)
html = html.replace('+919876543210', '+918019589810')
html = html.replace('+91 98765 43210', '+91 80195 89810')
html = html.replace('tel:+919876543210', 'tel:+918019589810')
html = html.replace('https://wa.me/919876543210', 'https://wa.me/918019589810')
print("✓ Phone numbers updated")

# 3. Update email
html = html.replace('info@butterflybloomcdc.com', 'hello@butterflybloomcdc.com')
html = html.replace('mailto:info@butterflybloomcdc.com', 'mailto:hello@butterflybloomcdc.com')
print("✓ Email updated")

# 4. Update location in contact section
old_location = '<p>Visakhapatnam<br>Andhra Pradesh, India</p>'
new_location = '<p>2nd Floor, Door No: 1, 53-8/2<br>Sector 1, MVP Colony<br>Visakhapatnam, AP 530017</p>'
html = html.replace(old_location, new_location)
print("✓ Location updated")

# 5. Update hours in contact section
old_hours = '<p>Mon - Sat: 9:00 AM - 6:00 PM<br>Sunday: By Appointment</p>'
new_hours = '<p>Mon - Sat: 9:00 AM - 7:00 PM<br>Sunday: By Appointment<br><strong>📅 On Appointment Basis Only</strong><br>Limited slots per week</p>'
html = html.replace(old_hours, new_hours)
print("✓ Hours updated")

# 6. Update closing time in schema (18:00 to 19:00)
html = html.replace('"closes": "18:00"', '"closes": "19:00"')
print("✓ Schema closing time updated")

# 7. Update address in schema
old_schema_address = '''"address": {
        "@type": "PostalAddress",
        "addressLocality": "Visakhapatnam",
        "addressRegion": "Andhra Pradesh",
        "addressCountry": "IN"
      }'''

new_schema_address = '''"address": {
        "@type": "PostalAddress",
        "streetAddress": "2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony",
        "addressLocality": "Visakhapatnam",
        "addressRegion": "Andhra Pradesh",
        "postalCode": "530017",
        "addressCountry": "IN"
      }'''

html = html.replace(old_schema_address, new_schema_address)
print("✓ Schema address updated")

# 8. Update "Team trained" to "Team served"
html = html.replace('<p>Team trained in USA, UK, and across India</p>', 
                    '<p>Team served to USA, UK, and across India</p>')
print("✓ Team description updated")

# Write the updated HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ All updates completed successfully!")
print("\nUpdated details:")
print("- Instagram: @butterflybloom_cdc")
print("- Phone: +91-8019589810")
print("- Email: hello@butterflybloomcdc.com")
print("- Location: 2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony, Visakhapatnam, AP 530017")
print("- Hours: Mon-Sat 9 AM - 7 PM, Sunday by appointment")
print("- Note: On appointment basis only, limited slots per week")
