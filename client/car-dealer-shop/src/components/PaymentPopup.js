import React, { useState } from "react";
import './payment.css'

const PaymentPopup = ({ handlePayment }) => {
  const [cardNumber, setCardNumber] = useState("");
  const [expiryDate, setExpiryDate] = useState("");
  const [cvv, setCVV] = useState("");

  const handleCardNumberChange = (e) => {
    setCardNumber(e.target.value);
  };

  const handleExpiryDateChange = (e) => {
    setExpiryDate(e.target.value);
  };

  const handleCVVChange = (e) => {
    setCVV(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Perform validation and payment processing logic here

    // Reset form fields
    setCardNumber("");
    setExpiryDate("");
    setCVV("");

    // Call the handlePayment function passed as a prop
    handlePayment();
  };

  return (
    <div className="payment-popup">
      <h2>Payment</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="cardNumber">Card Number:</label>
          <input
            type="text"
            id="cardNumber"
            value={cardNumber}
            onChange={handleCardNumberChange}
          />
        </div>
        <div>
          <label htmlFor="expiryDate">Expiry Date:</label>
          <input
            type="text"
            id="expiryDate"
            value={expiryDate}
            onChange={handleExpiryDateChange}
          />
        </div>
        <div>
          <label htmlFor="cvv">CVV:</label>
          <input
            type="text"
            id="cvv"
            value={cvv}
            onChange={handleCVVChange}
          />
        </div>
        <button type="submit">Pay Now</button>
      </form>
    </div>
  );
};

export default PaymentPopup;
