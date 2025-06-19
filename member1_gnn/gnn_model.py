# gnn_model.py — inside member1_gnn
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data
import pandas as pd
import os

# 🧠 Dummy Model for Encrypted Traffic
class GNNModel(nn.Module):
    def __init__(self):
        super(GNNModel, self).__init__()
        self.conv1 = GCNConv(4, 16)
        self.conv2 = GCNConv(16, 2)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# 📥 Load synthetic CSV from member2_rl
if not os.path.exists("dataset.csv"):
    print("❌ ERROR: dataset.csv not found. Run member2_rl/simulate.py first.")
    exit()

df = pd.read_csv("dataset.csv")
print("✅ Dataset loaded. Shape:", df.shape)

# ✨ Dummy graph: Connect each node to next (line graph)
edge_index = torch.tensor([[i, i+1] for i in range(len(df)-1)], dtype=torch.long).t().contiguous()

# 🔢 Features: pick 3 numeric fields
x = torch.tensor(df[['pkt_size', 'duration', 'seq','ack']].values, dtype=torch.float)
y = torch.tensor(df['label'].values, dtype=torch.long)

data = Data(x=x, edge_index=edge_index, y=y)

# 🧠 Train Model
model = GNNModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
loss_fn = nn.CrossEntropyLoss()

model.train()
for epoch in range(10):
    optimizer.zero_grad()
    out = model(data)
    loss = loss_fn(out, data.y)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# 💾 Save model
torch.save(model.state_dict(), "trained_model.pth")
print("✅ trained_model.pth saved successfully")


