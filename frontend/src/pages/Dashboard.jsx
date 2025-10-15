import React from "react";
import Navbar from "../components/Navbar";
import AdminSidebar from "../components/AdminSidebar";

const Dashboard = () => {
  return (
    <div className="flex min-h-screen">
      <AdminSidebar />
      <div className="flex-1 flex flex-col">
        <Navbar />
        <main className="flex-1 p-6">
          <h1 className="text-3xl font-bold mb-4">Dashboard</h1>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div className="bg-white shadow rounded p-4">Total Applications: 120</div>
            <div className="bg-white shadow rounded p-4">Pending Predictions: 45</div>
            <div className="bg-white shadow rounded p-4">Approved Loans: 75</div>
          </div>
          <div className="mt-6 bg-white p-4 rounded shadow">
            <h2 className="text-xl font-semibold mb-2">Recent Activities</h2>
            <ul className="list-disc list-inside text-gray-700">
              <li>User John submitted a loan application</li>
              <li>Prediction for user Mary completed</li>
              <li>Admin updated credit scoring parameters</li>
            </ul>
          </div>
        </main>
      </div>
    </div>
  );
};

export default Dashboard;