import { Route, Routes } from "react-router-dom";

// components
import Home from "./components/Home";
import Products from "./components/Products";
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
        <Route path="/products" element={<Products />} />

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
