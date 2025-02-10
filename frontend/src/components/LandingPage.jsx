import React from 'react';
import Navbar from './Navbar';
import Navbar2 from './NavBar_v2';

const LandingPage = () => {
  return (
    <div className="min-h-screen flex flex-col bg-gray-100">
      {/* Navbar */}
      <Navbar />
      <Navbar2 />
      {/* Contenido principal */}
      <div className="flex-grow flex flex-col items-center justify-center w-full px-4">
        <img
          src="https://via.placeholder.com/300"
          alt="Logo"
          className="mb-8 w-48 h-48 md:w-64 md:h-64"
        />

        <input
          type="text"
          placeholder="Busca aquí..."
          className="w-full max-w-2xl px-6 py-4 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 text-lg"
        />
      </div>
    </div>
  );
};

export default LandingPage;
