import React, { useState } from 'react';
import './login.css';

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [dateOfBirth, setDateOfBirth] = useState('');
  const [email, setEmail] = useState('');
  const [isSigningUp, setIsSigningUp] = useState(false);
  const [error, setError] = useState('');

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
    setError('');
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
      setError('Please provide all the required information.');
      return;
    }

    if (!username || !password) {
      setError('Please provide your username and password.');
      return;
    }

    setError('');

    if (isSigningUp) {
      // Perform signup logic here
      try {
        const response = await fetch('http://127.0.0.1:5000/buyers', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password, name, dateOfBirth, email }),
        });

        if (response.ok) {
          // User signed up successfully
          alert('Successfully signed up!');
          window.location.href = './home';
        } else {
          const errorData = await response.json();
          setError(errorData.message || 'Failed to sign up.');
        }
      } catch (error) {
        console.log('Error:', error);
        setError('Failed to sign up. Please try again later.');
      }
    } else {
      // Perform login logic here
      try {
        const response = await fetch('http://127.0.0.1:5000/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
          // User logged in successfully
          alert('Successfully logged in!');
          window.location.href = './home';
        } else {
          const errorData = await response.json();
          setError(errorData.message || 'Failed to log in.');
        }
      } catch (error) {
        console.log('Error:', error);
        setError('Failed to log in. Please try again later.');
      }
    }
  };

  return (
    <form
      className="login-form"
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
      {error && <p className="error-message">{error}</p>}
      <button type="submit">{isSigningUp ? 'Sign Up' : 'Login'}</button>
      <br />
      <button type="button" onClick={handleToggleSignup}>
        {isSigningUp ? 'Switch to Login' : 'Switch to Sign Up'}
      </button>
    </form>
  );
};

export default LoginForm;
