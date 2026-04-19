# routes.py

ROUTES = {
    "bus_1": {
        "name": "Gate → Library → Hostel",
        # These are the actual road coordinates (corners/turns)
        "waypoint_path": [
            [17.3850, 78.4867], [17.3855, 78.4870], [17.3860, 78.4880], 
            [17.3870, 78.4890], [17.3875, 78.4895], [17.3880, 78.4905],
            [17.3885, 78.4910], [17.3895, 78.4920], [17.3900, 78.4925]
        ],
        "stops": [
            {"name": "Main Gate", "index": 0}, 
            {"name": "Library", "index": 4},
            {"name": "Hostel Block A", "index": 8}
        ]
    },
    "bus_2": {
        "name": "Gate → Labs → Sports Ground",
        "waypoint_path": [
            [17.3850, 78.4867], [17.3845, 78.4875], [17.3840, 78.4885],
            [17.3835, 78.4895], [17.3830, 78.4900], [17.3825, 78.4910],
            [17.3820, 78.4920]
        ],
        "stops": [
            {"name": "Main Gate", "index": 0},
            {"name": "ECE Labs", "index": 4},
            {"name": "Sports Ground", "index": 6}
        ]
    }
}