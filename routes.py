# routes.py

ROUTES = {
    "bus_1": {
        "name": "Main Gate → Library → E-Block",
        "color": "#38bdf8",
        "waypoint_path": [
            [17.3917, 78.3262], [17.3915, 78.3255], [17.3912, 78.3245], # Entrance Road
            [17.3918, 78.3238], [17.3925, 78.3235], # Curve near Canteen
            [17.3932, 78.3230], [17.3940, 78.3228]  # Heading to Library/Hostels
        ],
        "stops": [
            {"name": "Main Gate", "index": 0},
            {"name": "Canteen", "index": 3},
            {"name": "Library", "index": 6}
        ]
    },
    "bus_2": {
        "name": "Gate → ECE Labs → Sports",
        "color": "#f472b6",
        "waypoint_path": [
            [17.3917, 78.3262], [17.3910, 78.3265], [17.3900, 78.3270], # Lower perimeter road
            [17.3892, 78.3275], [17.3885, 78.3280], 
            [17.3880, 78.3290] 
        ],
        "stops": [
            {"name": "Main Gate", "index": 0},
            {"name": "ECE Labs", "index": 3},
            {"name": "Sports Ground", "index": 5}
        ]
    }
}