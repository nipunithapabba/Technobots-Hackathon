# simulator.py
import asyncio
import time
import random
from routes import ROUTES

# Tracks current state of each bus
# Note: "route" must match the keys in routes.py ("bus_1", "bus_2")
bus_state = {
    "bus_1": {"route": "bus_1", "stop_index": 0, "progress": 0.0, "speed": 0.01},
    "bus_2": {"route": "bus_2", "stop_index": 0, "progress": 0.0, "speed": 0.008},
}

def interpolate(stop_a, stop_b, progress):
    """Calculate a position between two points based on progress (0.0 to 1.0)"""
    lat = stop_a["lat"] + (stop_b["lat"] - stop_a["lat"]) * progress
    lng = stop_a["lng"] + (stop_b["lng"] - stop_a["lng"]) * progress
    return lat, lng

# Global variable for weather (affects UI and ETA)
current_weather = "Rainy" 

def get_bus_positions():
    """Return current GPS position and occupancy of all buses"""
    positions = {}
    for bus_id, state in bus_state.items():
        # Safeguard: Check if route exists in ROUTES
        if state["route"] not in ROUTES:
            continue
            
        route = ROUTES[state["route"]]
        path = route["waypoint_path"]
        i = state["stop_index"]

        # Ensure we loop back to start if we exceed path length
        if i >= len(path) - 1:
            state["stop_index"] = 0
            state["progress"] = 0.0
            i = 0

        # Define points to move between
        stop_a = {"lat": path[i][0], "lng": path[i][1]}
        stop_b = {"lat": path[i+1][0], "lng": path[i+1][1]}
        
        lat, lng = interpolate(stop_a, stop_b, state["progress"])

        # Determine which stop is coming up next
        stops = route.get("stops", [])
        next_stop_name = "End of Route"
        for s in stops:
            if s["index"] > i:
                next_stop_name = s["name"]
                break

        # Generate live data fields
        occupancy = random.choice(["Low", "Medium", "High"])

        positions[bus_id] = {
            "bus_id": bus_id,
            "lat": round(lat, 6),
            "lng": round(lng, 6),
            "route_name": route["name"],
            "next_stop": next_stop_name,
            "occupancy": occupancy,
            "weather": current_weather,
            "timestamp": time.time()
        }

    return positions

def update_bus_positions():
    """Move each bus forward along the waypoints — call this every second"""
    for bus_id, state in bus_state.items():
        state["progress"] += state["speed"]

        # If reached next waypoint, advance to the following one
        if state["progress"] >= 1.0:
            state["progress"] = 0.0
            state["stop_index"] += 1

            # Check if we finished the whole path
            route_path = ROUTES[state["route"]]["waypoint_path"]
            if state["stop_index"] >= len(route_path) - 1:
                state["stop_index"] = 0
