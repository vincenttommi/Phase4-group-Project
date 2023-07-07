import React, { useState } from "react";
import { FaFacebook, FaTwitter, FaLinkedin, FaInstagram } from 'react-icons/fa';
import './footer.css';

const Footer = () => {
  const [comment, setComment] = useState('');
  const [commentsList, setCommentsList] = useState([]);

  const handleInputChange = (e) => {
    setComment(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (comment.trim() !== '') {
      setCommentsList([...commentsList, comment]);
      setComment('');
    }
  };

  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section">
          <h4>About Us</h4>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod magna sit amet nulla vestibulum euismod.</p>
        </div>
        <div className="footer-section">
          <h4>Contact Info</h4>
          <p>WESTLANDS</p>
          <p>kiambu,hapo rounda</p>
          <p>Email: Handlers@gmail.com</p>
          <p>Phone: +254 794471058</p>
        </div>
        <div className="footer-section">
          <h4>Follow Us</h4>
          <ul className="social-icons">
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
      <div className="comment-section">
        <h3>Leave a Comment</h3>
        <form onSubmit={handleSubmit}>
          <textarea
            value={comment}
            onChange={handleInputChange}
            placeholder="Write your comment here"
            rows={4}
          ></textarea>
          <button type="submit">Submit</button>
        </form>
        <div className="comment-list">
          <h3>Comments</h3>
          {commentsList.length === 0 ? (
            <p>No comments yet.</p>
          ) : (
            <ul>
              {commentsList.map((comment, index) => (
                <li key={index}>{comment}</li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </footer>
  );
};

export default Footer;
