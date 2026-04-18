<<<<<<< HEAD
 
=======
import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

records = []

for _ in range(2000):
    hour = random.randint(7, 20)
    day_of_week = random.randint(0, 6)
    stop_index = random.randint(0, 3)
    num_stops_remaining = 4 - stop_index
    network_quality = random.choice([0, 1])
    base_eta = num_stops_remaining * 3

    if (8 <= hour <= 10) or (16 <= hour <= 18):
        base_eta += random.uniform(2, 6)

    if day_of_week >= 5:
        base_eta -= random.uniform(0, 2)

    if network_quality == 0:
        base_eta += random.uniform(-1, 3)

    base_eta += random.uniform(-1, 2)
    base_eta = max(1, round(base_eta, 2))

    records.append({
        "hour": hour,
        "day_of_week": day_of_week,
        "stop_index": stop_index,
        "num_stops_remaining": num_stops_remaining,
        "network_quality": network_quality,
        "eta_minutes": base_eta
    })

df = pd.DataFrame(records)
df.to_csv("ml/historical_data.csv", index=False)
print(f"✅ Generated {len(df)} records")
print(df.head(10))
>>>>>>> e8a28f5dd3dc573d51eb2d78344a3838d350f529
