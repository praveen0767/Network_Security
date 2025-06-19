import React from "react";

function Dashboard() {
  return (
    <div className="max-w-4xl mx-auto space-y-8">
      <div className="p-6 border border-red-500 shadow-2xl bg-gray-800/80 rounded-2xl backdrop-blur-md">
        <h2 className="mb-2 text-2xl font-bold text-red-400">📦 Detected Threats</h2>
        <ul className="space-y-1 list-disc list-inside">
          <li>Encrypted threat at edge node 12.45.23.1</li>
          <li>GNN anomaly: Packet size deviation detected</li>
        </ul>
      </div>

      <div className="p-6 border border-green-500 shadow-2xl bg-gray-800/80 rounded-2xl backdrop-blur-md">
        <h2 className="mb-2 text-2xl font-bold text-green-400">🔄 Self-Healing Status</h2>
        <p className="text-green-300">Flow 2095 rerouted and isolated successfully. No action needed.</p>
      </div>

      <div className="p-6 border border-blue-500 shadow-2xl bg-gray-800/80 rounded-2xl backdrop-blur-md">
        <h2 className="mb-2 text-2xl font-bold text-blue-400">📈 System Logs</h2>
        <p className="text-sm text-gray-200">[03:45 AM] Reinforcement agent blocked novel AI threat</p>
        <p className="text-sm text-gray-200">[03:48 AM] Dashboard updated with latest healing actions</p>
      </div>
    </div>
  );
}

export default Dashboard;
