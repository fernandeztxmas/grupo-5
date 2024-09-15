import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ProductosList from './pages/ProductoList'; 
import CrearProducto from './pages/CrearProducto';
import ModificarProducto from './pages/ModificarProducto';
import ProductoDetalle from './pages/ProductoDetalle'; 

const App = () => {
  
  return (
    <Router>
      <div>
        <h1>Gestión de Productos</h1>
        <Routes>
          <Route path="/" element={<ProductosList />} />
          <Route path="/crear" element={<CrearProducto />} />
          <Route path="/modificar/:id" element={<ModificarProducto />} />
          <Route path="/producto/:id" element={<ProductoDetalle />} />
        </Routes>

        <footer>
        <p>&copy; 2024 Grupo 5</p>
      </footer>
      </div>
    </Router>
    
  );
};

export default App;
