import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from './pages/Home/HomePage';
import { ProductsList } from './components/ProductList/ProductsList';
import ProductDetails from './pages/shashank/ProductDetails';
import ProductDetailPage from './pages/Product/ProductDetailPage';
import MyComponent from './pages/shashank/post';

function App() {

  return (
    <React.Fragment>
    <BrowserRouter>
     <Routes>
      <Route path="/" element={<HomePage />} />
      {/* <Route path="smartphones" element={<ProductDetailPage />} /> */}
      <Route path="postreq" element={<MyComponent />} />
      <Route path="productslist" element={<ProductsList />} />
      <Route path="/products/:id" element={<ProductDetails />} />
      <Route path="/productdetails/:id" element={<ProductDetailPage />} />
     </Routes>
    </BrowserRouter>
    </React.Fragment>
  )
}

export default App;
