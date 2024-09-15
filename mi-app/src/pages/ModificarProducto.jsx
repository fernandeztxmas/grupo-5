import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import ProductoForm from '../components/ProductoForm';

const ModificarProducto = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const handleSubmit = async (data) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/productos/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const result = await response.json();
        alert('Producto modificado con éxito');
        console.log('Producto modificado:', result);
        navigate('/');
      } else {
        const errorData = await response.json();
        throw new Error(`Error al modificar el producto: ${errorData.detail}`);
      }
    } catch (error) {
      console.error('Error al modificar el producto:', error);
      alert(`Hubo un error al modificar el producto: ${error.message}`);
    }
  };

  return (
    <div>
      <h2>Modificar Producto</h2>
      <ProductoForm onSubmit={handleSubmit} productId={id} />
    </div>
  );
};

export default ModificarProducto;
