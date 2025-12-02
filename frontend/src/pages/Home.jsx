import React from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import LoanForm from "../components/LoanForm";
import PredictionResult from "../components/PredictionResult";

const Home = () => {
  const [result, setResult] = React.useState(null);

  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />

      <main className="flex-1 container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-center mb-6">
          AI-Powered Loan Approval
        </h1>
        
        <div className="max-w-2xl mx-auto">
          <LoanForm setResult={setResult} />
          <PredictionResult result={result} />
        </div>
      </main>

      <Footer />
    </div>
  );
};

export default Home;