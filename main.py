# main.py

import asyncio
import time
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from simulator import get_bus_positions, update_bus_positions
from buffer import add_to_buffer, flush_buffer, buffer_size
from routes import ROUTES

# Background task that updates bus positions every second
async def position_updater():
    while True:
        update_bus_positions()
        positions = get_bus_positions()
        add_to_buffer(positions)  # Always buffer in case client is offline
        await asyncio.sleep(1)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start background updater when server starts
    task = asyncio.create_task(position_updater())
    yield
    task.cancel()

app = FastAPI(title="Technobots Bus Tracker", lifespan=lifespan)

# Allow frontend to talk to this backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────
# ENDPOINTS
# ─────────────────────────────────────────────

@app.get("/")
def root():
    return {"message": "Technobots Bus Tracker API is running 🚌"}


@app.get("/buses")
def get_buses(network: str = Query(default="good")):
    """
    Returns live bus positions.
    network param: 'good' = full data, 'poor' = minimal data (adaptive payload)
    """
    positions = get_bus_positions()

    if network == "poor":
        # Low bandwidth mode — send only essential fields
        minimal = {}
        for bus_id, data in positions.items():
            minimal[bus_id] = {
                "bus_id": data["bus_id"],
                "lat": data["lat"],
                "lng": data["lng"]
            }
        return {"mode": "low_bandwidth", "buses": minimal}

    # Full data for good network
    return {"mode": "full", "buses": positions}


@app.get("/routes")
def get_routes():
    """Returns all route info with stops"""
    return {"routes": ROUTES}


@app.get("/sync")
def sync_offline_data():
    """
    Call this when client reconnects after being offline.
    Returns all buffered pings since disconnection.
    """
    buffered = flush_buffer()
    return {
        "message": f"Synced {len(buffered)} buffered updates",
        "buffered_pings": buffered
    }


@app.get("/status")
def server_status():
    """Health check + buffer info"""
    return {
        "status": "online",
        "buffer_size": buffer_size(),
        "timestamp": time.time()
    }


@app.get("/eta")
def get_eta(bus_id: str, stop_name: str):
    """
    Placeholder ETA endpoint — Member 2 will connect the real ML model here.
    For now returns a dummy estimate.
    """
    return {
        "bus_id": bus_id,
        "destination": stop_name,
        "eta_minutes": 4,
        "confidence": "placeholder — ML model pending"
    }
