# routes.py
ROUTES = {
    "bus_1": {
        "name": "Gate → Library → E-Block",
        "waypoint_path": [
            [17.3912, 78.3190], [17.3915, 78.3185], [17.3918, 78.3180], 
            [17.3922, 78.3178], [17.3928, 78.3175], [17.3935, 78.3172]
        ],
        "stops": [{"name": "Main Gate", "index": 0}, {"name": "Library", "index": 3}, {"name": "E-Block", "index": 5}]
    },
    "bus_2": {
        "name": "Gate → ECE → Sports",
        "waypoint_path": [
            [17.3912, 78.3190], [17.3908, 78.3195], [17.3902, 78.3200], 
            [17.3895, 78.3205], [17.3890, 78.3210]
        ],
        "stops": [{"name": "Main Gate", "index": 0}, {"name": "ECE Block", "index": 2}, {"name": "Sports Court", "index": 4}]
    }
}