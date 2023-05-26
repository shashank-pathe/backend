import React, { useState, useEffect } from 'react';
import { fetchProduct } from '../../services/api';
import { useParams } from 'react-router-dom';


const ProductDetails = () => {
  const [product, setProduct] = useState(null);
  const { id } = useParams();
  useEffect(() => {
    const fetchData = async () => {
 
      const data = await fetchProduct(id);
      
      setProduct(data);
    };

    fetchData();
  }, [id]);

  if (!product) {
    return <p>Loading product...</p>;
  }

  return (
    <div>
      <h3>{product.name}</h3>
      <p>Category: {product.category}</p>
      <p>Description: {product.description}</p>
      <img src={product.image} alt={product.name} />
      <p>Price: ${product.price}</p>
    </div>
  );
};

export default ProductDetails;
