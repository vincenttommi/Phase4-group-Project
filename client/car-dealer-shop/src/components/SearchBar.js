import React, { useState } from 'react';
import './main.css'

const SearchBar = ({ carModels, onSearch }) => {
  const [searchQuery, setSearchQuery] = useState('');

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
    </div>
  );
};

export default SearchBar;

