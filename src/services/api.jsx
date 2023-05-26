export const apiUrl = 'https://shashankpathe1.pythonanywhere.com/api';

export const getProducts = async () => {
  const response = await fetch(`${apiUrl}/products/`);
  console.log("shashank..............................................................................................................")
  const data = await response.json();
  return data;
};

export const fetchProduct = async (productId) => {
  try {
    const response = await fetch(`${apiUrl}/products/${productId}/`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching product:', error);
    return null;
  }
};


export const addToCart = async (productId, quantity) => {
  const response = await fetch(`${apiUrl}/cart`, {
    method: 'POST',
    body: JSON.stringify({ productId, quantity }),
    headers: { 'Content-Type': 'application/json' }
  });
  const data = await response.json();
  return data;

};

export const checkout = async (order) => {
  const response = await fetch(`${apiUrl}/checkout`, {
    method: 'POST',
    body: JSON.stringify(order),
    headers: { 'Content-Type': 'application/json' }
  });
  const data = await response.json();
  return data;
};
