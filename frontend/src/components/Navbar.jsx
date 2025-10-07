import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-blue-600 text-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          {/* Logo */}
          <div className="flex-shrink-0 flex items-center">
            <Link to="/" className="text-xl font-bold">
              CrediAI
            </Link>
          </div>

          {/* Links */}
          <div className="hidden md:flex md:items-center md:space-x-6">
            <Link to="/" className="hover:text-gray-200">
              Home
            </Link>
            <Link to="/dashboard" className="hover:text-gray-200">
              Dashboard
            </Link>
            <Link to="/applications" className="hover:text-gray-200">
              Applications
            </Link>
            <Link to="/predictions" className="hover:text-gray-200">
              Predictions
            </Link>
            <Link to="/login" className="hover:text-gray-200">
              Login
            </Link>
          </div>

          {/* Mobile menu button */}
          <div className="flex items-center md:hidden">
            {/* Placeholder for mobile menu icon */}
            <button className="p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-white">
              <svg
                className="h-6 w-6"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;