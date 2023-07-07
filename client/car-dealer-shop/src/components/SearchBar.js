import React, { useState, useEffect } from 'react';
import './main.css';

const SearchBar = ({ carModels, onSearch }) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  useEffect(() => {
    if (searchQuery.trim() !== '') {
      fetchSearchResults();
    } else {
      setSearchResults([]);
    }
  }, [searchQuery]);

  const fetchSearchResults = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/cars/search?query=${searchQuery}`);
      if (response.ok) {
        const data = await response.json();
        setSearchResults(data.results);
      } else {
        console.log('Failed to fetch search results');
      }
    } catch (error) {
      console.log('Error:', error);
    }
  };

  const handleSearch = (e) => {
    const query = e.target.value;
    setSearchQuery(query);
    onSearch(query);
  };

  return (
    <div className="searchbar">
      <input
        type="text"
        placeholder="Search car models..."
        value={searchQuery}
        onChange={handleSearch}
        className="searchbar-input searchbar-input--custom"
      />
      <ul className="search-results">
        {searchResults.map((result) => (
          <li key={result.id}>{result.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default SearchBar;
