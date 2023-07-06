import React from "react";
import { FaFacebook, FaTwitter, FaLinkedin, FaInstagram } from 'react-icons/fa';
import './footer.css';

const Footer = () => {
  return (
<footer className="footer">
  <div class="footer-content">
    <div class="footer-section">
      <h4>About Us</h4>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod magna sit amet nulla vestibulum euismod.</p>
    </div>
    <div class="footer-section">
      <h4>Contact Info</h4>
      <p>WESTLANDS</p>
      <p>kiambu,hapo rounda</p>
      <p>Email: Handlers@gmail.com</p>
      <p>Phone: +254 794471058</p>
    </div>
    <div class="footer-section">
      <h4>Follow Us</h4>
      <ul class="social-icons">
        <li><a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer"><FaFacebook /></a></li>
        <li><a href="https://www.twitter.com/" target="_blank" rel="noopener noreferrer"><FaTwitter /></a></li>
        <li><a href="https://www.linkedin.com/" target="_blank" rel="noopener noreferrer"><FaLinkedin /></a></li>
        <li><a href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer"><FaInstagram /></a></li>
      </ul>
    </div>
    <div className="col">
      <h4>Managerial Staff</h4>
      <h1>CEO's</h1>
      <p>1. TAMMY BRIGS</p>
      <p>2. VINCENT OMWAMI</p>
      <p>3. COLLINS KIMANI</p>
      <p>4. MELVIN JAMES</p>
    </div>
    <div className="footer-bottom">
      <h4>Secretary</h4>
      <p>MARGRET ACHIENG</p>
      <p>© 2024 NOVA CAR DEALERS</p>
    </div>
  </div>
</footer>

  );
}

export default Footer;
