import { Link } from 'react-router-dom';
import ProductosList from './ProductoList';

const Home = () => {
    return (
        <div style={{ display: "flex", alignItems: "center", flexDirection: "column"}}>
            <h1>Proyecto Base usando React</h1>
            {/* Aquí añadiremos el contenido de esta página, 
            incluyendo componentes como: Links, Listados, Forms u otros */}
            <ProductosList />
        </div>
    );
};

export default Home;