import React, { useState } from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import LoginForm from './components/LoginForm';
import Footer from './components/Footer';
import Cart from './components/cart';


function App() {
  const [setLoginFormVisible] = useState(false);
  const handleLoginClick = () => {
    setLoginFormVisible(true);
  };

  return (
    <Router>
      <div>
        <Navbar onLoginClick={handleLoginClick} />
        <Routes>
          <Route path="/Home" element={<Home/>} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/cart" element={<Cart />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
