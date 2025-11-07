
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.min.css';

if (!process.env.REACT_APP_CODESPACE_NAME) {
  const codespaceMatch = window.location.hostname.match(/^([^-]+)-8000\.app\.github\.dev$/);
  if (codespaceMatch) {
    process.env.REACT_APP_CODESPACE_NAME = codespaceMatch[1];
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
