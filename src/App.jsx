import { Route, Routes } from "react-router-dom";

// components
import Home from "./components/Home";
import Products from "./components/Products";
import ProductDetails from "./components/ProductDetails";
import ProductCatalog from "./components/ProductCatalog";
import Footer from "./components/Footer";
import Login from "./components/Login";
import Register from "./components/Register";
import AuthLandingPage from "./authcomponents/AuthLandingPage";

import "./App.css";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />

        <Route element={<Products />}>
          <Route path="/products" element={<ProductCatalog />} />
          <Route path="/products/:id" element={<ProductDetails />} />
        </Route>

        {/* route and subroutes of user */}

        {/* Auth */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Routes of authenticated users */}
        <Route path="/landingpage" element={<AuthLandingPage />} />
      </Routes>
      <Footer />
    </>
  );
}

export default App;
