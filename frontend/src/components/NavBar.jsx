import React from 'react';

const Navbar = () => {
  return (
    <nav className="bg-blue-600 text-white shadow-md fixed w-full z-10 top-0 left-0">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex items-center">
            <span className="text-2xl font-bold">MiLogo</span>
          </div>

          {/* Enlaces */}
          <div className="hidden md:flex space-x-8">
            <a href="#" className="hover:bg-blue-500 px-4 py-2 rounded-md text-lg">Inicio</a>
            <a href="#" className="hover:bg-blue-500 px-4 py-2 rounded-md text-lg">Servicios</a>
            <a href="#" className="hover:bg-blue-500 px-4 py-2 rounded-md text-lg">Contacto</a>
            <a href="#" className="hover:bg-blue-500 px-4 py-2 rounded-md text-lg">Acerca de</a>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
