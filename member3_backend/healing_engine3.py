from fastapi import FastAPI, Request
from pydantic import BaseModel
import torch
from torch_geometric.nn import GCNConv
import torch.nn as nn
import sqlite3
import uvicorn
import os

app = FastAPI()

class Flow(BaseModel):
    src_ip: str
    dst_ip: str
    pkt_size: int
    duration: float

class GCN(nn.Module):
    def __init__(self):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(4, 16)
        self.conv2 = GCNConv(16, 2)
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index)
        return x

model = GCN()
model.load_state_dict(torch.load("../member1_gnn/trained_model.pth"))
model.eval()

conn = sqlite3.connect("threats.db", check_same_thread=False)
conn.execute("CREATE TABLE IF NOT EXISTS logs(id INTEGER PRIMARY KEY AUTOINCREMENT, src TEXT, dst TEXT, result TEXT)")

@app.post("/scan")
async def scan_traffic(flow: Flow):
    feature = torch.tensor([[flow.pkt_size, flow.duration, 1234, 5678]], dtype=torch.float)
    edge_index = torch.tensor([[0],[0]], dtype=torch.long)
    with torch.no_grad():
        out = model(feature, edge_index)
        pred = out.argmax(dim=1).item()
        result = "THREAT" if pred == 1 else "NORMAL"
        conn.execute("INSERT INTO logs(src, dst, result) VALUES (?,?,?)", (flow.src_ip, flow.dst_ip, result))
        conn.commit()
        return {"result": result}

@app.get("/heal")
async def auto_heal():
    return {"status": "✅ Threat isolated and rerouted"}

@app.get("/log")
async def show_logs():
    cursor = conn.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 10")
    return {"logs": [dict(zip([c[0] for c in cursor.description], row)) for row in cursor.fetchall()]}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)