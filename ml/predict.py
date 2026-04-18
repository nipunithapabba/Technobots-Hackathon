<<<<<<< HEAD
 
=======
import joblib
import pandas as pd
import os
from datetime import datetime

MODEL_PATH = os.path.join(os.path.dirname(__file__), "bus_eta_model.pkl")
model = joblib.load(MODEL_PATH)

def predict_eta(stop_index: int, network_quality: int = 1) -> dict:
    now = datetime.now()
    hour = now.hour
    day_of_week = now.weekday()
    num_stops_remaining = max(1, 4 - stop_index)

    input_data = pd.DataFrame([{
        "hour": hour,
        "day_of_week": day_of_week,
        "stop_index": stop_index,
        "num_stops_remaining": num_stops_remaining,
        "network_quality": network_quality
    }])

    eta = model.predict(input_data)[0]
    eta = round(max(1.0, eta), 1)

    if (8 <= hour <= 10) or (16 <= hour <= 18):
        condition = "Rush hour — slight delays expected"
    elif day_of_week >= 5:
        condition = "Weekend — lighter traffic"
    else:
        condition = "Normal conditions"

    network_note = "Live data" if network_quality == 1 else "Estimated (poor network)"

    return {
        "eta_minutes": eta,
        "stops_remaining": num_stops_remaining,
        "condition": condition,
        "network_note": network_note,
        "predicted_at": now.strftime("%H:%M:%S")
    }


if __name__ == "__main__":
    print("🧪 Testing predictions:\n")
    test_cases = [
        {"stop_index": 0, "network_quality": 1},
        {"stop_index": 2, "network_quality": 1},
        {"stop_index": 0, "network_quality": 0},
        {"stop_index": 3, "network_quality": 1},
    ]
    for case in test_cases:
        result = predict_eta(**case)
        print(f"  Stop {case['stop_index']} | Network {'Good' if case['network_quality'] else 'Poor'}")
        print(f"  → ETA: {result['eta_minutes']} mins | {result['condition']}")
        print(f"  → {result['network_note']}\n")
>>>>>>> e8a28f5dd3dc573d51eb2d78344a3838d350f529
