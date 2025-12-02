import React from "react";

const Footer = () => {
  return (
    <footer className="bg-blue-600 text-white py-6 mt-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row justify-between items-center">
        {/* Left side */}
        <div className="text-center md:text-left">
          <p className="text-sm">&copy; 2025 CrediAI. All rights reserved.</p>
        </div>

        {/* Right side */}
        <div className="mt-4 md:mt-0 flex space-x-4">
          <a
            href="#"
            className="text-white hover:text-gray-200 text-sm"
            target="_blank"
            rel="noopener noreferrer"
          >
            Privacy Policy
          </a>
          <a
            href="#"
            className="text-white hover:text-gray-200 text-sm"
            target="_blank"
            rel="noopener noreferrer"
          >
            Terms of Service
          </a>
          <a
            href="#"
            className="text-white hover:text-gray-200 text-sm"
            target="_blank"
            rel="noopener noreferrer"
          >
            Contact
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;