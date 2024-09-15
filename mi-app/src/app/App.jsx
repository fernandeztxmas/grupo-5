import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import AppRouter from './Router';


const App = () => {
  return (
    <Router>
      <div>
        <h1>Gestión de Productos</h1>
        <AppRouter />
        <footer>
          <p>&copy; 2024 Grupo 5 🧙‍♂️</p>
        </footer>
      </div>
    </Router>
  );
};

export default App;
