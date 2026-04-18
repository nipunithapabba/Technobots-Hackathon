import requests
import time

BASE = "http://127.0.0.1:8000"

PASS = "✅"
FAIL = "❌"

def test(label, condition):
    status = PASS if condition else FAIL
    print(f"  {status} {label}")
    return condition

print("\n🧪 TECHNOBOTS INTEGRATION TEST SUITE")
print("=" * 45)

print("\n📡 1. Server Health")
try:
    r = requests.get(f"{BASE}/", timeout=5)
    test("Server is online", r.status_code == 200)
    test("Returns message", "message" in r.json())
except Exception as e:
    print(f"  {FAIL} Server unreachable: {e}")

print("\n🚌 2. Bus Positions (Full Network)")
try:
    r = requests.get(f"{BASE}/buses?network=good", timeout=5)
    data = r.json()
    test("Status 200", r.status_code == 200)
    test("Returns buses key", "buses" in data)
    test("Has bus_1", "bus_1" in data["buses"])
    test("Has bus_2", "bus_2" in data["buses"])
    test("Mode is full", data["mode"] == "full")
    bus = data["buses"]["bus_1"]
    test("bus_1 has lat", "lat" in bus)
    test("bus_1 has lng", "lng" in bus)
    test("bus_1 has route_name", "route_name" in bus)
    test("bus_1 has next_stop", "next_stop" in bus)
except Exception as e:
    print(f"  {FAIL} Error: {e}")

print("\n📶 3. Low Bandwidth Mode")
try:
    r = requests.get(f"{BASE}/buses?network=poor", timeout=5)
    data = r.json()
    test("Status 200", r.status_code == 200)
    test("Mode is low_bandwidth", data["mode"] == "low_bandwidth")
    bus = data["buses"]["bus_1"]
    test("Minimal payload has lat", "lat" in bus)
    test("Minimal payload has lng", "lng" in bus)
    test("Minimal payload has NO route_name", "route_name" not in bus)
except Exception as e:
    print(f"  {FAIL} Error: {e}")

print("\n🗺️  4. Route Data")
try:
    r = requests.get(f"{BASE}/routes", timeout=5)
    data = r.json()
    test("Status 200", r.status_code == 200)
    test("Has routes key", "routes" in data)
    test("Has route_1", "route_1" in data["routes"])
    test("Has route_2", "route_2" in data["routes"])
    stops = data["routes"]["route_1"]["stops"]
    test("Route 1 has stops", len(stops) > 0)
    test("Each stop has lat/lng", "lat" in stops[0] and "lng" in stops[0])
except Exception as e:
    print(f"  {FAIL} Error: {e}")

print("\n⏱️  5. ML ETA Prediction")
try:
    r = requests.get(f"{BASE}/eta?bus_id=bus_1&stop_index=1&network=good", timeout=5)
    data = r.json()
    test("Status 200", r.status_code == 200)
    test("Has eta_minutes", "eta_minutes" in data)
    test("ETA is positive number", data["eta_minutes"] > 0)
    test("Has condition field", "condition" in data)
    test("Has network_note", "network_note" in data)
    r2 = requests.get(f"{BASE}/eta?bus_id=bus_1&stop_index=1&network=poor", timeout=5)
    data2 = r2.json()
    test("Poor network ETA works", "eta_minutes" in data2)
    test("Poor network note different", data2["network_note"] != data["network_note"])
except Exception as e:
    print(f"  {FAIL} Error: {e}")

print("\n📦 6. Store & Forward Buffer")
try:
    print("  ⏳ Waiting 3s for buffer to collect pings...")
    time.sleep(3)
    r = requests.get(f"{BASE}/status", timeout=5)
    data = r.json()
    test("Status endpoint works", r.status_code == 200)
    test("Buffer size is tracked", "buffer_size" in data)
    test("Buffer has collected pings", data["buffer_size"] > 0)
    r2 = requests.get(f"{BASE}/sync", timeout=5)
    data2 = r2.json()
    test("Sync endpoint works", r2.status_code == 200)
    test("Returns buffered pings", "buffered_pings" in data2)
    test("Has synced pings", len(data2["buffered_pings"]) > 0)
    print(f"  ℹ️  Synced {len(data2['buffered_pings'])} buffered pings")
except Exception as e:
    print(f"  {FAIL} Error: {e}")

print("\n🔄 7. Live Movement")
try:
    r1 = requests.get(f"{BASE}/buses", timeout=5)
    pos1 = r1.json()["buses"]["bus_1"]
    print("  ⏳ Waiting 3s for bus to move...")
    time.sleep(3)
    r2 = requests.get(f"{BASE}/buses", timeout=5)
    pos2 = r2.json()["buses"]["bus_1"]
    moved = pos1["lat"] != pos2["lat"] or pos1["lng"] != pos2["lng"]
    test("Bus position changed over time", moved)
except Exception as e:
    print(f"  {FAIL} Error: {e}")

print("\n" + "=" * 45)
print("🏁 Tests complete!\n")
