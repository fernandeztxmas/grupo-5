import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ProductosList from './componentes/ProductoList'; 
import CrearProducto from './componentes/CrearProducto';
import ModificarProducto from './componentes/ModificarProducto';
import ProductoDetalle from './componentes/ProductoDetalle'; 

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
      </div>
    </Router>
  );
};

export default App;
