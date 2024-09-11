import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const ProductosList = () => {
  const [productos, setProductos] = useState([]);

  useEffect(() => {
    cargarProductos();
  }, []);

  const cargarProductos = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/productos');
      const data = await response.json();
      setProductos(data);
    } catch (error) {
      console.error('Error al cargar los productos:', error);
    }
  };

  const eliminarProducto = async (id) => {
    if (!window.confirm('¿Estás seguro de que deseas eliminar este producto?')) {
      return;
    }

    try {
      await fetch(`http://127.0.0.1:8000/productos/${id}`, {
        method: 'DELETE',
      });
      alert('Producto eliminado con éxito');
      cargarProductos();
    } catch (error) {
      console.error('Error al eliminar el producto:', error);
      alert('Hubo un error al eliminar el producto.');
    }
  };

  return (
    <div>
      <h2>Lista de Productos</h2>
      <Link to="/crear">Crear Nuevo Producto</Link>
      <ul>
        {productos.map(producto => (
          <li key={producto.id}>
            {producto.nombre} - {producto.precio} - {producto.descripcion}
            <Link to={`/modificar/${producto.id}`}> Modificar</Link>
            <Link to={`/producto/${producto.id}`}> Ver Detalles</Link>
            <button onClick={() => eliminarProducto(producto.id)}>Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductosList;
