import React from "react";

const PredictionResult = ({ result }) => {
  if (!result) {
    return null; // No result to show
  }

  return (
    <div className="max-w-md mx-auto mt-6 bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-xl font-bold text-gray-800 mb-4">Loan Prediction Result</h2>
      
      <div className="flex justify-between items-center mb-2">
        <span className="font-semibold text-gray-700">Approval Status:</span>
        <span className={`font-bold ${result.approved ? "text-green-600" : "text-red-600"}`}>
          {result.approved ? "Approved ✅" : "Denied ❌"}
        </span>
      </div>

      <div className="flex justify-between items-center mb-2">
        <span className="font-semibold text-gray-700">Predicted Probability:</span>
        <span className="text-gray-800">{(result.probability * 100).toFixed(2)}%</span>
      </div>

      {result.recommendations && result.recommendations.length > 0 && (
        <div className="mt-4">
          <h3 className="font-semibold text-gray-700 mb-2">Recommendations:</h3>
          <ul className="list-disc list-inside text-gray-700">
            {result.recommendations.map((rec, index) => (
              <li key={index}>{rec}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default PredictionResult;