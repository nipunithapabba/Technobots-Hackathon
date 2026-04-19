# 🚌 CampusCruise — Campus Bus Tracker
### ThinkRoot x Vortex Hackathon 2026 — Track B

A resilient real-time public transport tracking system for college campuses that works reliably even under low bandwidth and high latency conditions.

---

## 🚀 Live Demo

| | Link |
|--|------|
| **Frontend App** | https://nipunithapabba.github.io/Technobots-Hackathon/ |
| **Documentation Site** | https://campuscruise-docs-27d87e-z4x0a.thinkroot.app/ |
| **Backend API** | https://technobots-bus-tracker.onrender.com |
| **API Docs** | https://technobots-bus-tracker.onrender.com/docs |
| **GitHub Repo** | https://github.com/nipunithapabba/Technobots-Hackathon |

---

## 👥 Team — Technobots

| Member | Role | GitHub |
|--------|------|--------|
| Bollena Chervitha | Backend Developer (FastAPI, Simulator, Buffer) | [@chervitha22](https://github.com/chervitha22) |
| Renu Priya Molgara | ML Engineer (ETA Prediction Model) | [@renupriyamolgara-web](https://github.com/renupriyamolgara-web) |
| Vuppula Nishitha | Frontend Developer (Map UI, ThinkRoot) | [@vuppulanishitha12](https://github.com/vuppulanishitha12) |
| Nipunitha Pabba | Integration, Deployment & Testing | [@nipunithapabba](https://github.com/nipunithapabba) |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Backend | Python, FastAPI | REST API and bus simulation |
| ML Model | scikit-learn (Random Forest) | ETA prediction from historical data |
| Frontend | HTML, CSS, Leaflet.js | Interactive real-time map UI |
| Deployment — Backend | Render.com | Free cloud hosting |
| Deployment — Frontend | GitHub Pages | Static site hosting |
| Documentation | ThinkRoot | Hackathon platform requirement |
| Version Control | GitHub | Team collaboration |

---

## ⚙️ Key Features

- **Live GPS Simulation** — 2 buses moving along real Osmania University road paths
- **Road-Following Buses** — bus markers snap to and follow actual campus road coordinates
- **Adaptive Payloads** — smaller data packets on poor networks (`?network=poor`)
- **Store & Forward Buffer** — GPS pings saved during disconnect, synced on reconnect
- **ML ETA Prediction** — Random Forest model trained on 2000 historical trips (MAE ~0.8 min, R² ~0.97)
- **Stop ETA Popup** — click any stop on the map to see live ETA for all buses
- **Network Status Badge** — Live / Offline / Syncing shown in real time
- **Collapsible Sidebar** — clean UI with dark/light theme toggle
- **27/27 Integration Tests Passing** — fully verified end-to-end

---

## 🏃 Run Locally

### Backend
```bash
pip install -r requirements.txt
python ml/generate_data.py
python ml/train_model.py
uvicorn main:app --reload
```

### Frontend
Open `frontend/index.html` in your browser or visit the GitHub Pages link above.

---

## 📡 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Server health check |
| `GET /buses` | Live bus positions (full payload) |
| `GET /buses?network=poor` | Minimal payload for low bandwidth |
| `GET /routes` | All routes and stops |
| `GET /eta?bus_id=bus_1&stop_index=1&network=good` | ML-powered ETA prediction |
| `GET /sync` | Flush buffered offline pings |
| `GET /status` | Server health and buffer size |
| `GET /docs` | Interactive Swagger API documentation |

---

## 🧪 Testing

```bash
# Full integration test suite (27 tests)
python test_integration.py

# Network resilience demo
python simulate_network_drop.py
```

### Test Results
```
✅ Server Health         — 2/2 passing
✅ Bus Positions         — 5/5 passing
✅ Low Bandwidth Mode    — 3/3 passing
✅ Route Data            — 4/4 passing
✅ ML ETA Prediction     — 5/5 passing
✅ Store & Forward       — 5/5 passing
✅ Live Movement         — 1/1 passing
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total: 27/27 passing ✅
```

---

## 📁 Project Structure

```
Technobots-Hackathon/
├── main.py                    # FastAPI server
├── routes.py                  # Bus route definitions
├── simulator.py               # GPS position simulator
├── buffer.py                  # Store & forward buffer
├── requirements.txt           # Python dependencies
├── render.yaml                # Render deployment config
├── test_integration.py        # Integration test suite
├── simulate_network_drop.py   # Resilience demo script
├── ml/
│   ├── generate_data.py       # Training data generation
│   ├── train_model.py         # Random Forest model training
│   ├── predict.py             # ETA prediction function
│   └── bus_eta_model.pkl      # Trained model file
└── frontend/
    └── index.html             # Complete frontend app
```
