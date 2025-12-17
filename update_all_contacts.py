import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Update Instagram handle (both URL and display text)
html_content = html_content.replace(
    'https://www.instagram.com/butterflybloom.cdc',
    'https://www.instagram.com/butterflybloom_cdc'
)
html_content = html_content.replace(
    '@butterflybloom.cdc',
    '@butterflybloom_cdc'
)

# Update phone number
html_content = html_content.replace(
    '+919876543210',
    '+918019589810'
)
html_content = html_content.replace(
    '+91 98765 43210',
    '+91 80195 89810'
)

# Update email
html_content = html_content.replace(
    'info@butterflybloomcdc.com',
    'hello@butterflybloomcdc.com'
)

# Update location
html_content = html_content.replace(
    '<p>Visakhapatnam<br>Andhra Pradesh, India</p>',
    '<p>2nd Floor, Door No: 1, 53-8/2<br>Sector 1, MVP Colony<br>Visakhapatnam, AP 530017</p>'
)

# Update hours
html_content = html_content.replace(
    '<p>Mon - Sat: 9:00 AM - 6:00 PM<br>Sunday: By Appointment</p>',
    '<p>Mon - Sat: 9:00 AM - 7:00 PM<br>Sunday: By Appointment<br><strong>📅 Appointment Basis Only</strong><br>Limited slots per week</p>'
)

# Update closing time in schema
html_content = html_content.replace(
    '"closes": "18:00"',
    '"closes": "19:00"'
)

# Update "Team trained" to "Team served"
html_content = html_content.replace(
    '<p>Team trained in USA, UK, and across India</p>',
    '<p>Team served to USA, UK, and across India</p>'
)

# Update address in schema - add street address and postal code
address_pattern = r'"address": \{\s*"@type": "PostalAddress",\s*"addressLocality": "Visakhapatnam",\s*"addressRegion": "Andhra Pradesh",\s*"addressCountry": "IN"\s*\}'
new_address = '''"address": {
        "@type": "PostalAddress",
        "streetAddress": "2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony",
        "addressLocality": "Visakhapatnam",
        "addressRegion": "Andhra Pradesh",
        "postalCode": "530017",
        "addressCountry": "IN"
      }'''
html_content = re.sub(address_pattern, new_address, html_content)

# Write the updated HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ All updates completed successfully!")
print("- Instagram handle updated to @butterflybloom_cdc")
print("- Phone number updated to +91 80195 89810")
print("- Email updated to hello@butterflybloomcdc.com")
print("- Address updated with full details")
print("- Hours updated to 9 AM - 7 PM")
print("- Team description updated to 'served'")
