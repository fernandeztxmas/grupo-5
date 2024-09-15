import { Link } from 'react-router-dom';
import ProductosList from './ProductoList';

const Home = () => {
    return (
        <div style={{ display: "flex", alignItems: "center", flexDirection: "column"}}>
            <h1>Proyecto Base usando React</h1>
            {/* No supe que poner acá xd*/}
            <ProductosList />
        </div>
    );
};

export default Home;