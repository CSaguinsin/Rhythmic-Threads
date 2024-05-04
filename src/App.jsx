import './App.css'

import { BrowserRouter as  Router, Route, Routes} from 'react-router-dom';

// components
import Home from './components/Home'
import Navbar from './components/Navbar'
import Footer from './components/Footer';
function App() {

  return (
    <>
    <Navbar />
    <Routes>
      <Route path='/' element={<Home />} />
    </Routes>
    <Footer />
    </>
  )
}

export default App
