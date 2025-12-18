const fs = require('fs');

// Read the file
let content = fs.readFileSync('index.html', 'utf8');

// 1. Update Instagram handle
content = content.replace(/butterflybloom\.cdc/g, 'butterflybloom_cdc/');
content = content.replace(/@butterflybloom\.cdc/g, '@butterflybloom_cdc');

// 2. Update phone number
content = content.replace(/\+919876543210/g, '+918019589810');
content = content.replace(/\+91 98765 43210/g, '+91 80195 89810');

// 3. Update email
content = content.replace(/info@butterflybloomcdc\.com/g, 'hello@butterflybloomcdc.com');

// 4. Update address in schema
content = content.replace(
  '"addressLocality": "Visakhapatnam",',
  '"streetAddress": "2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony",\n        "addressLocality": "Visakhapatnam",\n        "postalCode": "530017",'
);

// 5. Update hours in schema
content = content.replace('"closes": "18:00"', '"closes": "19:00"');

// 6. Update location in contact section
content = content.replace(
  '<p>Visakhapatnam<br>Andhra Pradesh, India</p>',
  '<p>2nd Floor, Door No: 1, 53-8/2<br>Sector 1, MVP Colony<br>Visakhapatnam, AP 530017</p>'
);

// 7. Update hours in contact section
content = content.replace(
  '<p>Mon - Sat: 9:00 AM - 6:00 PM<br>Sunday: By Appointment</p>',
  '<p>Mon - Sat: 9:00 AM - 7:00 PM<br>Sunday: By Appointment<br><strong>📅 On Appointment Basis Only</strong></p>'
);

// Write the updated content
fs.writeFileSync('index.html', content, 'utf8');

console.log('✅ Contact details updated successfully!');
console.log('\nUpdated:');
console.log('- Instagram: @butterflybloom_cdc (with trailing slash)');
console.log('- Phone: +91-8019589810');
console.log('- Email: hello@butterflybloomcdc.com');
console.log('- Address: 2nd Floor, Door No: 1, 53-8/2, Sector 1, MVP Colony, Visakhapatnam, AP 530017');
console.log('- Hours: Mon-Sat 9 AM - 7 PM (On appointment basis only)');
