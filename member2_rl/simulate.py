import pandas as pd
import random

flows = []
for i in range(300):
    normal = {
        'pkt_size': random.randint(200, 1400),
        'duration': round(random.uniform(0.3, 5.0), 2),
        'seq': random.randint(1000, 9999),
        'ack': random.randint(1000, 9999),
        'label': 0  # 0 = normal
    }
    attack = {
        'pkt_size': random.randint(1000, 1600),
        'duration': round(random.uniform(2.5, 8.0), 2),
        'seq': random.randint(10000, 99999),
        'ack': random.randint(10000, 99999),
        'label': 1  # 1 = attack
    }
    flows.append(normal)
    flows.append(attack)

pd.DataFrame(flows).to_csv('synthetic_flows.csv', index=False)
print("✅ Synthetic traffic generated (saved as synthetic_flows.csv)")