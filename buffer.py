# buffer.py

from collections import deque
import time

# Stores pings when client is offline (max 100 entries)
offline_buffer = deque(maxlen=100)

def add_to_buffer(positions: dict):
    """Save a snapshot of positions to the buffer"""
    offline_buffer.append({
        "timestamp": time.time(),
        "positions": positions
    })

def flush_buffer():
    """Return all buffered pings and clear the buffer"""
    data = list(offline_buffer)
    offline_buffer.clear()
    return data

def buffer_size():
    return len(offline_buffer) 
