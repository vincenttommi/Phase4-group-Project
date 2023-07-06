import React from 'react';
import './contact.css'

const ContactUs = () => {
  return (
    <div>
      <h1>Contact Us Page</h1>
      <h2>Contact Information</h2>
      <table>
        <thead>
          <tr>
            <th>Office</th>
            <th>Contact Number</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Nairobi Office</td>
            <td>+254 123 4567</td>
            <td>info@nairobioffice.com</td>
          </tr>
          <tr>
            <td>Kisumu Office</td>
            <td>+254 987 6543</td>
            <td>info@kisumuoffice.com</td>
          </tr>
          <tr>
            <td>Embu Office</td>
            <td>+254 567 8901</td>
            <td>info@embuoffice.com</td>
          </tr>
          <tr>
            <td>Mombasa Office</td>
            <td>+254 234 5678</td>
            <td>info@mombasaoffice.com</td>
          </tr>
        </tbody>
      </table>

      <h2>Working Hours</h2>
      <table>
        <thead>
          <tr>
            <th>Office</th>
            <th>Monday-Friday</th>
            <th>Saturday</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Nairobi Office</td>
            <td>9:00 AM - 6:00 PM</td>
            <td>9:00 AM - 2:00 PM</td>
          </tr>
          <tr>
            <td>Kisumu Office</td>
            <td>8:30 AM - 5:30 PM</td>
            <td>9:00 AM - 1:00 PM</td>
          </tr>
          <tr>
            <td>Embu Office</td>
            <td>8:00 AM - 5:00 PM</td>
            <td>Closed</td>
          </tr>
          <tr>
            <td>Mombasa Office</td>
            <td>9:30 AM - 6:30 PM</td>
            <td>10:00 AM - 3:00 PM</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default ContactUs;
