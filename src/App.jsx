import './App.css'

import { BrowserRouter as  Router, Route, Routes} from 'react-router-dom';

// components
import Home from './components/Home'
import Footer from './components/Footer';

// auth components
import AuthLandingPage from './authcomponents/AuthLandingPage';
function App() {

  return (
    <>
    <Routes>
      <Route path='/' element={<Home />} />


      {/* Routes of authenticated users */}
      <Route path='/landingpage' element={<AuthLandingPage />} />
    </Routes>
    <Footer />
    </>)
}

export default App
