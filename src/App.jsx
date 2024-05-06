import { Route, Routes } from "react-router-dom";

// components
import Home from "./components/Home";
import Footer from "./components/Footer";
import AuthLandingPage from "./authcomponents/AuthLandingPage";
import "./App.css";

// auth components
function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />

        {/* Routes of authenticated users */}
        <Route path="/landingpage" element={<AuthLandingPage />} />
      </Routes>
      <Footer />
    </>
  );
}

export default App;
