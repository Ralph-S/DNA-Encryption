import { Route, Routes } from "react-router-dom";
import Footer from "../components/Footer/Footer";
import Hero from "../components/Hero/Hero"
import Navbar from "../components/Navbar/Navbar";
import Secrets from "../components/Secrets/secrets";


function RouterProvider() {

  return (
    <div className="content">
      <Navbar />
      <Routes>
        <Route path="/" element={<Hero />} />
        <Route path="/secrets" element={<Secrets />} />
  
      </Routes>
      <Footer />
    </div>
  );
}

export default RouterProvider;