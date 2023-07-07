import React, { useState } from 'react';
import { Carousel } from 'react-responsive-carousel';
import { Link } from 'react-router-dom';
import SearchBar from './SearchBar';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import './home.css';
import Card from './card';

const Home = () => {
  const [filteredCarModels, setFilteredCarModels] = useState([]);
  const [showSearchBar, setShowSearchBar] = useState(true);
  const [cartItems, setCartItems] = useState([]);

  const carModels = ['Honda', 'Toyota', 'Ford', 'Chevrolet', 'BMW'];

  const searchCarModels = (query) => {
    const filteredModels = carModels.filter((model) =>
      model.toLowerCase().includes(query.toLowerCase())
    );
    setFilteredCarModels(filteredModels);
  };

  const handleSearchToggle = () => {
    setShowSearchBar(!showSearchBar);
  };

  const slides = [
    {
      title: 'mustang',
      imageUrl: 'https://images.unsplash.com/photo-1602200059552-39ed78989991?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxjb2xsZWN0aW9uLXRodW1ibmFpbHx8MTE1ODU0OXx8ZW58MHx8fHx8&dpr=1&auto=format&fit=crop&w=294&h=294&q=60',
      description: 'mustang',
    },
    {
      title: 'Slide 2',
      imageUrl: 'https://images.unsplash.com/photo-1687166783902-45947281f59d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxjb2xsZWN0aW9uLXRodW1ibmFpbHx8OHBnYVh4SV9jcFV8fGVufDB8fHx8fA%3D%3D&dpr=1&auto=format&fit=crop&w=294&h=294&q=60',
    },
    {
      title: 'Slide 3',
      imageUrl: 'https://images.unsplash.com/photo-1612882834894-8205a248a74a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxjb2xsZWN0aW9uLXRodW1ibmFpbHx8ODUzNTgzMXx8ZW58MHx8fHx8&dpr=1&auto=format&fit=crop&w=294&h=294&q=60',
    },
    {
      title: 'Slide 4',
      imageUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQRt9Aq-BdZyFx76uswomU8AgYZVJM7ahcSSgnHyYZHeR6odvZAfD3ZyRXLlhxrUy-uKw&usqp=CAU',
    },
    {
      title: 'Slide 5',
      imageUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOpeHatY4_TXeOgRdJmM9-NIGNt5VtP26KFKE3Jl3rS2ELA44yaWFTOX0tA5Hf5r1cIJY&usqp=CAU',
    },
    {
      title: 'Slide 6',
      imageUrl: 'https://images.unsplash.com/photo-1526726538690-5cbf956ae2fd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGNhcnN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60',
    },
    {
      title: 'Slide 6',
      imageUrl: '',
    },
  ];

  const addToCart = (car) => {
    setCartItems([...cartItems, car]);
  };

  return (
    <div className="home-container">
      <h1 className="home-title">Welcome to Nova Dealers</h1>

      <Carousel showThumbs={false}>
        {slides.map((slide, index) => (
          <div key={index}>
            <img src={slide.imageUrl} alt={slide.title} />
            <p className="legend">{slide.description}</p>
          </div>
        ))}
      </Carousel>

      {showSearchBar && (
        <SearchBar carModels={carModels} onSearch={searchCarModels} />
      )}

      <button onClick={handleSearchToggle} className="home-search-toggle">
        {showSearchBar ? 'Hide Search Bar' : 'Show Search Bar'}
      </button>

      {filteredCarModels.map((model) => (
        <p key={model}>{model}</p>
      ))}

      <h2>Car Shop</h2>
      <div className="card-container">
        <Card carId={1} addToCart={addToCart} />
        <Card carId={2} addToCart={addToCart} />
        <Card carId={3} addToCart={addToCart} />
      </div>

      <h2>Cart</h2>
      <ul>
        {cartItems.map((car, index) => (
          <li key={index}>
            {car.car_make} {car.car_model}
          </li>
        ))}
      </ul>

      {/* Company Welcome */}
      <div className="company-welcome">
        <h2>Welcome to Nova Dealers</h2>
        <p>
          Nova Dealers is your go-to destination for high-quality cars. We offer a wide selection of vehicles from top manufacturers. Whether you're looking for a reliable sedan or a luxurious SUV, we have the perfect car for you. Browse our inventory and find your dream car today.
        </p>
      </div>

      {/* Read More Button */}
      <Link to="/about" className="read-more-button">
        Read More
      </Link>

      {/* Add more elements as needed */}
    </div>
  );
};

export default Home;
