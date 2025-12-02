import React from "react";

const UserCard = ({ user }) => {
  return (
    <div className="bg-white p-4 rounded-lg shadow-md flex items-center space-x-4">
      <img
        src={user.avatar || "/assets/default-avatar.png"}
        alt={user.name}
        className="w-12 h-12 rounded-full object-cover"
      />
      <div>
        <h3 className="font-semibold text-gray-800">{user.name}</h3>
        <p className="text-gray-600 text-sm">{user.email}</p>
        <p className="text-gray-600 text-sm">Credit Score: {user.creditScore}</p>
      </div>
    </div>
  );
};

export default UserCard;