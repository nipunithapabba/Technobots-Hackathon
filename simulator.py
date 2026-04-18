# simulator.py

import asyncio
import time
from routes import ROUTES

# Tracks current state of each bus
bus_state = {
    "bus_1": {"route": "route_1", "stop_index": 0, "progress": 0.0, "speed": 0.01},
    "bus_2": {"route": "route_2", "stop_index": 0, "progress": 0.0, "speed": 0.008},
}

def interpolate(stop_a, stop_b, progress):
    """Calculate a position between two stops based on progress (0.0 to 1.0)"""
    lat = stop_a["lat"] + (stop_b["lat"] - stop_a["lat"]) * progress
    lng = stop_a["lng"] + (stop_b["lng"] - stop_a["lng"]) * progress
    return lat, lng

def get_bus_positions():
    """Return current GPS position of all buses"""
    positions = {}
    for bus_id, state in bus_state.items():
        route = ROUTES[state["route"]]
        stops = route["stops"]
        i = state["stop_index"]

        # If bus reached the last stop, loop back to start
        if i >= len(stops) - 1:
            state["stop_index"] = 0
            state["progress"] = 0.0
            i = 0

        stop_a = stops[i]
        stop_b = stops[i + 1]
        lat, lng = interpolate(stop_a, stop_b, state["progress"])

        positions[bus_id] = {
            "bus_id": bus_id,
            "lat": round(lat, 6),
            "lng": round(lng, 6),
            "route": state["route"],
            "route_name": route["name"],
            "next_stop": stop_b["name"],
            "timestamp": time.time()
        }

    return positions

def update_bus_positions():
    """Move each bus forward a little — call this every second"""
    for bus_id, state in bus_state.items():
        state["progress"] += state["speed"]

        # If reached next stop, advance to the following stop
        if state["progress"] >= 1.0:
            state["progress"] = 0.0
            state["stop_index"] += 1

            route_stops = ROUTES[state["route"]]["stops"]
            if state["stop_index"] >= len(route_stops) - 1:
                state["stop_index"] = 0
