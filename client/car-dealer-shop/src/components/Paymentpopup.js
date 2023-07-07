import React from "react";

const PaymentPopup = ({ handlePayment }) => {
  // Implement payment form and functionality here

  return (
    <div className="payment-popup">
      <h2>Payment</h2>
      {/* Implement payment form */}
      <button onClick={handlePayment}>Pay Now</button>
    </div>
  );
};

export default PaymentPopup;
