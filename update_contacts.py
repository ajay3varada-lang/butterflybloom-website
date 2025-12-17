import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Update phone number in contact section
html_content = html_content.replace(
    '<a href="tel:+919876543210">+91 98765 43210</a>',
    '<a href="tel:+918019589810">+91 80195 89810</a>'
)

# Update email in contact section
html_content = html_content.replace(
    '<a href="mailto:info@butterflybloomcdc.com">info@butterflybloomcdc.com</a>',
    '<a href="mailto:hello@butterflybloomcdc.com">hello@butterflybloomcdc.com</a>'
)

# Update location in contact section
html_content = html_content.replace(
    '<p>Visakhapatnam<br>Andhra Pradesh, India</p>',
    '<p>2nd Floor, Door No: 1, 53-8/2<br>Sector 1, MVP Colony<br>Visakhapatnam, AP 530017</p>'
)

# Update hours in contact section
html_content = html_content.replace(
    '<p>Mon - Sat: 9:00 AM - 6:00 PM<br>Sunday: By Appointment</p>',
    '<p>Mon - Sat: 9:00 AM - 7:00 PM<br>Sunday: By Appointment<br><strong>Appointment Basis Only</strong><br>Limited slots per week</p>'
)

# Update WhatsApp link
html_content = html_content.replace(
    '<a href="https://wa.me/919876543210" target="_blank">Chat with us instantly</a>',
    '<a href="https://wa.me/918019589810" target="_blank">Chat with us instantly</a>'
)

# Update Schema.org phone and email
html_content = html_content.replace(
    '"telephone": "+919876543210"',
    '"telephone": "+918019589810"'
)
html_content = html_content.replace(
    '"email": "info@butterflybloomcdc.com"',
    '"email": "hello@butterflybloomcdc.com"'
)

# Update Schema.org address
address_pattern = r'"address": \{[^}]+\}'
new_address = '''"address": {
        "@type": "PostalAddress",
        "streetAddress": "2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony",
        "addressLocality": "Visakhapatnam",
        "addressRegion": "Andhra Pradesh",
        "postalCode": "530017",
        "addressCountry": "IN"
      }'''
html_content = re.sub(address_pattern, new_address, html_content)

# Update Schema.org opening hours
html_content = html_content.replace(
    '"closes": "18:00"',
    '"closes": "19:00"'
)

# Write the updated HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Contact details updated successfully!")
