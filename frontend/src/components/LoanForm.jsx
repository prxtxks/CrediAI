import React, { useState } from "react";

const LoanForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    income: "",
    loanAmount: "",
    creditScore: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Pass data to parent or API call
    onSubmit(formData);
  };

  return (
    <form
      className="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md space-y-4"
      onSubmit={handleSubmit}
    >
      <h2 className="text-xl font-bold text-gray-800 mb-4">Apply for a Loan</h2>

      <input
        type="text"
        name="fullName"
        placeholder="Full Name"
        value={formData.fullName}
        onChange={handleChange}
        className="w-full p-2 border border-gray-300 rounded"
        required
      />

      <input
        type="email"
        name="email"
        placeholder="Email Address"
        value={formData.email}
        onChange={handleChange}
        className="w-full p-2 border border-gray-300 rounded"
        required
      />

      <input
        type="number"
        name="income"
        placeholder="Annual Income ($)"
        value={formData.income}
        onChange={handleChange}
        className="w-full p-2 border border-gray-300 rounded"
        required
      />

      <input
        type="number"
        name="loanAmount"
        placeholder="Loan Amount ($)"
        value={formData.loanAmount}
        onChange={handleChange}
        className="w-full p-2 border border-gray-300 rounded"
        required
      />

      <input
        type="number"
        name="creditScore"
        placeholder="Credit Score"
        value={formData.creditScore}
        onChange={handleChange}
        className="w-full p-2 border border-gray-300 rounded"
        required
      />

      <button
        type="submit"
        className="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 transition"
      >
        Submit Application
      </button>
    </form>
  );
};

export default LoanForm;