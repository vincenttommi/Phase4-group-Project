import React, { useState } from 'react';
import './login.css';

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [dateOfBirth, setDateOfBirth] = useState('');
  const [email, setEmail] = useState('');
  const [isSigningUp, setIsSigningUp] = useState(false);

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleNameChange = (e) => {
    setName(e.target.value);
  };

  const handleDateOfBirthChange = (e) => {
    setDateOfBirth(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handleToggleSignup = () => {
    setIsSigningUp(!isSigningUp);

    // Clear the sign-up form fields when switching to login mode
    if (!isSigningUp) {
      setName('');
      setDateOfBirth('');
      setEmail('');
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (isSigningUp && (!name || !dateOfBirth || !email)) {
      alert('Please provide all the required information.');
      return;
    }

    if (!username || !password) {
      alert('Please provide your username and password.');
      return;
    }

    if (isSigningUp) {
      // Perform signup logic here
      try {
        // Make a request to the backend to create a new user
        const response = await fetch('http://127.0.0.1:5000/buyers', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password, name, dateOfBirth, email }),
        });

        if (response.ok) {
          // User signed up successfully
          alert('Successfully signed up!');
        } else {
          // Handle signup failure
          alert('Failed to sign up.');
        }
      } catch (error) {
        console.log('Error:', error);
      }
    } else {
      // Perform login logic here
      try {
        // Make a request to the backend to authenticate the user
        const response = await fetch('http://127.0.0.1:5000/buyers', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
          // User logged in successfully
          alert('Successfully logged in!');
        } else {
          // Handle login failure
          alert('Failed to log in.');
        }
      } catch (error) {
        console.log('Error:', error);
      }
    }

    window.location.href = './home';
  };

  return (
    <form className="login-form"
        onSubmit={handleSubmit}
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          marginTop: '1em',
        }}
      >
      <label>
        Username:
        <input type="text" value={username} onChange={handleUsernameChange} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={handlePasswordChange} />
      </label>
      <br />
      {isSigningUp && (
        <div className="signup-fields">
          <label>
            Name:
            <input type="text" value={name} onChange={handleNameChange} />
          </label>
          <br />
          <label>
            Date of Birth:
            <input type="date" value={dateOfBirth} onChange={handleDateOfBirthChange} />
          </label>
          <br />
          <label>
            Email Address:
            <input type="email" value={email} onChange={handleEmailChange} />
          </label>
          <br />
        </div>
      )}
      <button type="submit">{isSigningUp ? 'Sign Up' : 'Login'}</button>
      <br />
      <button type="button" onClick={handleToggleSignup}>
        {isSigningUp ? 'Switch to Login' : 'Switch to Sign Up'}
      </button>
    </form>
  );
};

export default LoginForm;
