import React from 'react';
import ProductoForm from './ProductoForm';

const CrearProducto = () => {
  /*const handleSubmit = async (data) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/productos', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const result = await response.json();
        alert('Producto creado con éxito');
        console.log('Producto creado:', result);
      } else {
        const errorData = await response.json();
        throw new Error(`Error al crear el producto: ${errorData.detail}`);
      }
    } catch (error) {
      console.error('Error al crear el producto:', error);
      alert(`Hubo un error al crear el producto: ${error.message}`);
    }
  }; */

  return (
    <div>
      <h2>Crear Producto</h2>
      <ProductoForm />
    </div>
  );
};

export default CrearProducto;
