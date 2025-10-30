import React, { useState } from "react";
import axios from "axios";
import PredictionResult from "../components/PredictionResult";

const Predictions = () => {
  const [formData, setFormData] = useState({
    income: "",
    loanAmount: "",
    creditScore: "",
    dependents: "",
    age: "",
  });

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await axios.post("http://localhost:5000/api/predict", formData);
      setResult(res.data);
    } catch (error) {
      console.error("Prediction Error:", error);
      setResult({ error: "Failed to fetch prediction." });
    }

    setLoading(false);
  };

  return (
    <div className="page predictions-page">
      <div className="container">
        <h1>AI Loan Prediction</h1>
        <p>Enter your details and let our AI model predict approval chances.</p>

        <form className="prediction-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Monthly Income</label>
            <input type="number" name="income" value={formData.income} onChange={handleChange} required />
          </div>

          <div className="form-group">
            <label>Loan Amount</label>
            <input type="number" name="loanAmount" value={formData.loanAmount} onChange={handleChange} required />
          </div>

          <div className="form-group">
            <label>Credit Score</label>
            <input type="number" name="creditScore" value={formData.creditScore} onChange={handleChange} required />
          </div>

          <div className="form-group">
            <label>Dependents</label>
            <input type="number" name="dependents" value={formData.dependents} onChange={handleChange} required />
          </div>

          <div className="form-group">
            <label>Age</label>
            <input type="number" name="age" value={formData.age} onChange={handleChange} required />
          </div>

          <button type="submit" disabled={loading}>
            {loading ? "Predicting..." : "Get Prediction"}
          </button>
        </form>

        {result && <PredictionResult result={result} />}
      </div>
    </div>
  );
};

export default Predictions;

// UI improvement pending review