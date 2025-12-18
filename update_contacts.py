#!/usr/bin/env python3
import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Instagram handle (butterflybloom.cdc -> butterflybloom_cdc)
content = content.replace('butterflybloom.cdc', 'butterflybloom_cdc')
content = content.replace('@butterflybloom.cdc', '@butterflybloom_cdc')

# 2. Update phone number
content = content.replace('+919876543210', '+918019589810')
content = content.replace('+91 98765 43210', '+91 80195 89810')

# 3. Update email
content = content.replace('info@butterflybloomcdc.com', 'hello@butterflybloomcdc.com')

# 4. Update address in schema - add street address and postal code
content = content.replace(
    '"addressLocality": "Visakhapatnam",',
    '"streetAddress": "2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony",\n        "addressLocality": "Visakhapatnam",\n        "postalCode": "530017",'
)

# 5. Update hours in schema (6 PM to 7 PM)
content = content.replace('"closes": "18:00"', '"closes": "19:00"')

# 6. Update location in contact section
content = content.replace(
    '<p>Visakhapatnam<br>Andhra Pradesh, India</p>',
    '<p>2nd Floor, Door No: 1, 53-8/2<br>Sector 1, MVP Colony<br>Visakhapatnam, AP 530017</p>'
)

# 7. Update hours in contact section with proper icon
content = content.replace(
    '<p>Mon - Sat: 9:00 AM - 6:00 PM<br>Sunday: By Appointment</p>',
    '<p>Mon - Sat: 9:00 AM - 7:00 PM<br>Sunday: By Appointment<br><strong>📅 On Appointment Basis Only</strong></p>'
)

# Write the updated content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Contact details updated successfully!')
print('\nUpdated:')
print('- Instagram: @butterflybloom_cdc')
print('- Phone: +91-8019589810')
print('- Email: hello@butterflybloomcdc.com')
print('- Address: 2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony, Visakhapatnam, AP 530017')
print('- Hours: Mon-Sat 9 AM - 7 PM (📅 On appointment basis only)')
