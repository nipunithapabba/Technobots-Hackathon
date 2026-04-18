import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("ml/historical_data.csv")

FEATURES = [
    "hour",
    "day_of_week",
    "stop_index",
    "num_stops_remaining",
    "network_quality"
]

X = df[FEATURES]
y = df["eta_minutes"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"✅ Model trained successfully!")
print(f"📊 Mean Absolute Error : {mae:.2f} minutes")
print(f"📊 R² Score            : {r2:.4f}")
print(f"   (R² closer to 1.0 = better model)")

importances = model.feature_importances_
print("\n🔍 Feature Importances:")
for feat, imp in sorted(zip(FEATURES, importances), key=lambda x: -x[1]):
    print(f"   {feat:<25} {imp:.4f}")

joblib.dump(model, "ml/bus_eta_model.pkl")
print("\n💾 Model saved to ml/bus_eta_model.pkl")