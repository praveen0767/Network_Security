// App.js
import React from "react";
import Dashboard from "./components/Dashboard";
import ThreatLogs from "./components/ThreatLogs";
import "./index.css";

function App() {
  return (
    <div className="min-h-screen p-6 text-white bg-gradient-to-b from-black via-gray-900 to-black">
      <h1 className="mb-10 text-4xl font-bold text-center animate-pulse text-cyan-400">
        🛡️ Wal Shiled
      </h1>
      <Dashboard />
      <div className="mt-12">
        <ThreatLogs />
      </div>
    </div>
  );
}

export default App;
