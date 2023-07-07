import React, { useState } from "react";
import PaymentPopup from "./PaymentPopup";

const Cart = ({ cart, removeFromCart }) => {
  const [showPaymentPopup, setShowPaymentPopup] = useState(false);
  const [showCart, setShowCart] = useState(false);
  const [showPayment, setShowPayment] = useState(false);

  const getTotalPrice = () => {
    return cart.reduce((total, car) => total + car.price, 0);
  };

  const handlePay = () => {
    setShowPaymentPopup(true);
  };

  const handlePayment = () => {
    // Implement payment functionality here
  };

  const toggleCart = () => {
    setShowCart(!showCart);
  };

  const togglePayment = () => {
    setShowPayment(!showPayment);
  };

  return (
    <div className="cart">
      <h2>Cart</h2>
      {cart && cart.length === 0 ? (
        <p>No items in the cart</p>
      ) : (
        <>
          {cart &&
            cart.map((car) => (
              <div className="cart-item" key={car.id}>
                <h3>{car.car_make}</h3>
                <p>{car.car_model}</p>
                <img src={car.car_image} alt="Car" />
                <button onClick={() => removeFromCart(car.id)}>Remove</button>
              </div>
            ))}
          <p>Total Price: ${getTotalPrice()}</p>
          <button onClick={handlePay}>Pay</button>
        </>
      )}
      {showPaymentPopup && (
        <div className="payment-popup">
          <h2>Payment</h2>
          {/* Display payment form and payment options */}
          <button onClick={handlePayment}>Make Payment</button>
        </div>
      )}
      <button onClick={toggleCart}>Toggle Cart</button>
      <button onClick={togglePayment}>Toggle Payment</button>
      {showCart && (
        <div>
          <h2>Cart</h2>
          <ul>
            {cart &&
              cart.map((car, index) => (
                <li key={index}>
                  {car.car_make} {car.car_model}
                </li>
              ))}
          </ul>
        </div>
      )}
      {showPayment && <PaymentPopup handlePayment={handlePayment} />}
    </div>
  );
};

export default Cart;
