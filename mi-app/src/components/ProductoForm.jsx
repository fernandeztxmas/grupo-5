import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';

const ProductoForm = ({ onSubmit, initialData = {}, productId }) => {
  const { control, handleSubmit, formState: { errors }, reset } = useForm({
    defaultValues: initialData,
  });

  const [isFetched, setIsFetched] = useState(false);
  const navigate = useNavigate(); // Hook para redirección

  useEffect(() => {
    if (productId && !isFetched) {
      fetch(`http://127.0.0.1:8000/productos/${productId}`)
        .then(response => response.json())
        .then(data => {
          reset(data);
          setIsFetched(true);
        })
        .catch(error => {
          console.error('Error al cargar el producto:', error);
        });
    }
  }, [productId, reset, isFetched]);

  const submitHandler = async (data) => {
    try {
      const payload = {
        nombre: data.nombre,
        precio: parseFloat(data.precio),
        descripcion: data.descripcion || '',
      };

      const url = productId
        ? `http://127.0.0.1:8000/productos/${productId}`
        : 'http://127.0.0.1:8000/productos';

      const method = productId ? 'PUT' : 'POST';

      const response = await fetch(url, {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      if (response.ok) {
        const result = await response.json();
        console.log('Producto guardado:', result);

        // Mostrar alerta de éxito
        alert('Producto creado exitosamente');
        
        // Redirigir al menú principal
        navigate('/');
      } else {
        const errorData = await response.json();
        throw new Error(`Error en la respuesta del servidor: ${response.status} - ${errorData.detail}`);
      }
    } catch (error) {
      console.error('Error al guardar el producto:', error);
      alert(`Hubo un error al guardar el producto: ${error.message}`);
    }
  };

  return (
    <div className="container">
      <h2>{productId ? 'Modificar Producto' : 'Crear Producto'}</h2>
      <form onSubmit={handleSubmit(submitHandler)}>
        <div>
          <label htmlFor="nombre">Nombre</label>
          <Controller
            name="nombre"
            control={control}
            rules={{ required: "El nombre es obligatorio" }}
            render={({ field }) => (
              <input
                id="nombre"
                type="text"
                {...field}
              />
            )}
          />
          {errors.nombre && <span className="message">{errors.nombre.message}</span>}
        </div>
  
        <div>
          <label htmlFor="precio">Precio</label>
          <Controller
            name="precio"
            control={control}
            rules={{
              required: "El precio es obligatorio",
              valueAsNumber: true,
              min: { value: 0, message: "El precio debe ser mayor o igual a 0" }
            }}
            render={({ field }) => (
              <input
                id="precio"
                type="number"
                step="0.01"
                {...field}
              />
            )}
          />
          {errors.precio && <span className="message">{errors.precio.message}</span>}
        </div>
  
        <div>
          <label htmlFor="descripcion">Descripción</label>
          <Controller
            name="descripcion"
            control={control}
            render={({ field }) => (
              <textarea
                id="descripcion"
                {...field}
              />
            )}
          />
        </div>
  
        <button type="submit">Guardar</button>
      </form>
    </div>
  );
};

export default ProductoForm;
