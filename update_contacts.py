#!/usr/bin/env python3
"""
Update contact details in index.html
- Instagram: @butterflybloom_cdc (with trailing slash)
- Phone: +91-8019589810
- Email: hello@butterflybloomcdc.com
- Address: 2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony, Visakhapatnam, AP 530017
- Hours: Mon-Sat 9 AM - 7 PM (On appointment basis only)
"""

import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Instagram handle (dot to underscore, add trailing slash)
content = content.replace('butterflybloom.cdc', 'butterflybloom_cdc/')
content = content.replace('@butterflybloom.cdc', '@butterflybloom_cdc')

# 2. Update phone number
content = content.replace('+919876543210', '+918019589810')
content = content.replace('+91 98765 43210', '+91 80195 89810')

# 3. Update email
content = content.replace('info@butterflybloomcdc.com', 'hello@butterflybloomcdc.com')

# 4. Update address in schema (add street address and postal code)
schema_address_old = '''      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Visakhapatnam",
        "addressRegion": "Andhra Pradesh",
        "addressCountry": "IN"
      },'''

schema_address_new = '''      "address": {
        "@type": "PostalAddress",
        "streetAddress": "2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony",
        "addressLocality": "Visakhapatnam",
        "postalCode": "530017",
        "addressRegion": "Andhra Pradesh",
        "addressCountry": "IN"
      },'''

content = content.replace(schema_address_old, schema_address_new)

# 5. Update hours in schema (6 PM to 7 PM)
content = content.replace('"closes": "18:00"', '"closes": "19:00"')

# 6. Update location in contact section
location_old = '<p>Visakhapatnam<br>Andhra Pradesh, India</p>'
location_new = '<p>2nd Floor, Door No: 1, 53-8/2<br>Sector 1, MVP Colony<br>Visakhapatnam, AP 530017</p>'
content = content.replace(location_old, location_new)

# 7. Update hours in contact section
hours_old = '<p>Mon - Sat: 9:00 AM - 6:00 PM<br>Sunday: By Appointment</p>'
hours_new = '<p>Mon - Sat: 9:00 AM - 7:00 PM<br>Sunday: By Appointment<br><strong>📅 On Appointment Basis Only</strong></p>'
content = content.replace(hours_old, hours_new)

# Write the updated content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Contact details updated successfully!")
print("\nUpdated:")
print("- Instagram: @butterflybloom_cdc (with trailing slash)")
print("- Phone: +91-8019589810")
print("- Email: hello@butterflybloomcdc.com")
print("- Address: 2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony, Visakhapatnam, AP 530017")
print("- Hours: Mon-Sat 9 AM - 7 PM (On appointment basis only)")
