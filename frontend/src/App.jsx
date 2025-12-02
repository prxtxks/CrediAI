import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Applications from "./pages/Applications";
import Predictions from "./pages/Predictions";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />

        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/applications" element={<Applications />} />
        <Route path="/predictions" element={<Predictions />} />

        {/* Fallback */}
        <Route path="*" element={<div className='p-10 text-center'>404 - Page Not Found</div>} />
      </Routes>
    </Router>
  );
};

export default App;