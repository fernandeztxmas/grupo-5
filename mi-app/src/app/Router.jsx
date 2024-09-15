import React from 'react';
import { Routes, Route } from 'react-router-dom';
import ProductosList from '../pages/ProductoList';
import CrearProducto from '../pages/CrearProducto';
import ModificarProducto from '../pages/ModificarProducto';
import ProductoDetalle from '../pages/ProductoDetalle';
import Layout from '../components/Layout';

const AppRouter = () => {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<ProductosList />} />
        <Route path="/crear" element={<CrearProducto />} />
        <Route path="/modificar/:id" element={<ModificarProducto />} />
        <Route path="/producto/:id" element={<ProductoDetalle />} />
      </Routes>
    </Layout>
  );
};

export default AppRouter;
