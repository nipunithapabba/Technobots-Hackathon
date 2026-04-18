import requests
import time

BASE = "https://technobots-bus-tracker.onrender.com"

print("\n🎬 NETWORK RESILIENCE DEMO")
print("=" * 40)

print("\n📡 Phase 1: Normal operation (3 pings)")
for i in range(3):
    r = requests.get(f"{BASE}/buses?network=good")
    buses = r.json()["buses"]
    bus1 = buses["bus_1"]
    print(f"  Ping {i+1}: bus_1 at ({bus1['lat']}, {bus1['lng']})")
    time.sleep(1)

print("\n🔴 Phase 2: Client goes OFFLINE (5 seconds)")
print("  [Frontend disconnected — backend keeps buffering]")
time.sleep(5)

print("\n📦 Checking buffer size during offline period...")
r = requests.get(f"{BASE}/status")
buf = r.json()["buffer_size"]
print(f"  Buffer collected {buf} pings while offline")

print("\n🟡 Phase 3: Client RECONNECTS — syncing buffered data")
r = requests.get(f"{BASE}/sync")
data = r.json()
pings = data["buffered_pings"]
print(f"  ✅ Synced {len(pings)} pings successfully")

if pings:
    print(f"\n  📍 First buffered position:")
    first = pings[0]["positions"]["bus_1"]
    print(f"     lat: {first['lat']}, lng: {first['lng']}")
    print(f"\n  📍 Last buffered position:")
    last = pings[-1]["positions"]["bus_1"]
    print(f"     lat: {last['lat']}, lng: {last['lng']}")

print("\n🟢 Phase 4: Back to normal operation")
r = requests.get(f"{BASE}/buses?network=good")
bus1 = r.json()["buses"]["bus_1"]
print(f"  Live position: ({bus1['lat']}, {bus1['lng']})")

print("\n✅ Resilience demo complete!\n")
