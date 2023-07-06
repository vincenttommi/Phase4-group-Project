import React from 'react';
import './main.css';

import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <img src='logo.png' alt="Company Logo" className="logo-image" />
        <p>
          <span className="company-name">NOVA DEALERS</span>
        </p>
        <p>
          <span className="company-salutation">Mapema Ndio Best</span>
        </p>
      </div>
      <ul className="navbar-list">
        <li className="navbar-item"><Link to="/home">Home</Link></li>
        <li className="navbar-item"><Link to="/about">About</Link></li>
        <li className="navbar-item"><Link to="/contact">Contact</Link></li>
        <li className="navbar-item"><Link to="/login">Login</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
