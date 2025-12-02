import React from "react";
import Navbar from "../components/Navbar";
import AdminSidebar from "../components/AdminSidebar";

const Applications = () => {
  const applications = [
    { id: 1, name: "John Doe", amount: 5000, status: "Pending" },
    { id: 2, name: "Mary Smith", amount: 10000, status: "Approved" },
    { id: 3, name: "David Lee", amount: 7500, status: "Rejected" },
  ];

  return (
    <div className="flex min-h-screen">
      <AdminSidebar />
      <div className="flex-1 flex flex-col">
        <Navbar />
        <main className="p-6">
          <h1 className="text-3xl font-bold mb-4">Loan Applications</h1>

          <div className="bg-white shadow rounded p-4">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="border-b">
                  <th className="p-3 font-semibold">Name</th>
                  <th className="p-3 font-semibold">Loan Amount</th>
                  <th className="p-3 font-semibold">Status</th>
                </tr>
              </thead>
              <tbody>
                {applications.map((app) => (
                  <tr key={app.id} className="border-b hover:bg-gray-50">
                    <td className="p-3">{app.name}</td>
                    <td className="p-3">${app.amount}</td>
                    <td
                      className={`p-3 font-semibold ${
                        app.status === "Approved"
                          ? "text-green-600"
                          : app.status === "Rejected"
                          ? "text-red-600"
                          : "text-yellow-600"
                      }`}
                    >
                      {app.status}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </main>
      </div>
    </div>
  );
};

export default Applications;