import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';

const ProductoDetalle = () => {
  const { id } = useParams();
  const [producto, setProducto] = useState(null);

  useEffect(() => {
    const cargarProducto = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/productos/${id}`);
        const data = await response.json();
        setProducto(data);
      } catch (error) {
        console.error('Error al cargar el producto:', error);
      }
    };

    cargarProducto();
  }, [id]);

  if (!producto) {
    return <p>Cargando...</p>;
  }

  return (
    <div>
      <h2>Detalles del Producto</h2>
      <p><strong>Nombre:</strong> {producto.nombre}</p>
      <p><strong>Precio:</strong> {producto.precio} €</p>
      <p><strong>Descripción:</strong> {producto.descripcion}</p>
      <Link to="/">Volver a la lista</Link>
    </div>
  );
};

export default ProductoDetalle;

