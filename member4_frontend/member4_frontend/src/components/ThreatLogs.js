// components/ThreatLogs.js
import React from "react";

const logs = [
  { id: 1, threat: "AI-Mutated Malware", status: "Blocked", time: "10:42 AM" },
  { id: 2, threat: "Unknown Packet Flow", status: "Isolated", time: "11:17 AM" },
];

const statusColor = {
  Blocked: "text-red-400",
  Isolated: "text-yellow-400",
};

const ThreatLogs = () => {
  return (
    <div className="max-w-4xl p-6 mx-auto border border-purple-500 shadow-2xl bg-gray-800/80 rounded-2xl backdrop-blur-md">
      <h2 className="mb-4 text-2xl font-bold text-purple-400">🔍 Threat Logs</h2>
      <table className="w-full overflow-hidden text-left border border-gray-600 rounded-lg">
        <thead className="bg-gray-700">
          <tr>
            <th className="p-3">ID</th>
            <th className="p-3">Threat</th>
            <th className="p-3">Status</th>
            <th className="p-3">Time</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log) => (
            <tr
              key={log.id}
              className="transition duration-300 border-t border-gray-600 hover:bg-gray-700"
            >
              <td className="p-3">{log.id}</td>
              <td className="p-3 font-semibold">{log.threat}</td>
              <td className={`p-3 font-bold ${statusColor[log.status]}`}>{log.status}</td>
              <td className="p-3">{log.time}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ThreatLogs;
