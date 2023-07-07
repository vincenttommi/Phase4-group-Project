import React, { useState, useEffect } from "react";

const Card = ({ carId, car_price, addToCart }) => {
  const [car, setCar] = useState(null);

  useEffect(() => {
    const fetchCarDetails = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:5000/cars/${carId}`);
        const data = await response.json();
        setCar({ ...data, car_price }); // Include car_price in the car object
      } catch (error) {
        console.log("Error fetching car details:", error);
      }
    };

    fetchCarDetails();
  }, [carId, car_price]);

  if (!car) {
    return <div>Loading...</div>;
  }

  return (
    <div className="car-card">
      <img src={car.image} alt={car.car_make} />
      <h3>{car.car_make} {car.car_model}</h3>
      <p>Year: {car.car_year}</p>
      <p>Price: 10000{car.car_price}</p>
      <button onClick={() => addToCart(car)}>Add to Cart</button>
    </div>
  );
};

export default Card;
