# 🚌 Technobots Bus Tracker
### ThinkRoot x Vortex Hackathon 2026 — Track B

A resilient real-time public transport tracking system for college campuses
that works reliably even under low bandwidth and high latency conditions.

---

## 🚀 Live Demo
- **Frontend:** [ThinkRoot Deployment URL - Coming Soon]
- **Backend API:** [Render Deployment URL - Coming Soon]
- **API Docs:** [Render Deployment URL - Coming Soon]/docs

---

## 👥 Team — Technobots
| Member | Role |
|--------|------|
| Member 1 | Backend (FastAPI, Simulator, Buffer) |
| Member 2 | ML (ETA Prediction Model) |
| Member 3 | Frontend (Map UI, ThinkRoot) |
| Member 4 | Integration, Deployment, Testing |

---

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Python, FastAPI |
| ML Model | scikit-learn (Random Forest) |
| Frontend | HTML, CSS, Leaflet.js |
| Deployment (Backend) | Render.com |
| Deployment (Frontend) | ThinkRoot |

---

## ⚙️ Key Features
- **Live GPS Simulation** — 2 buses moving along real campus routes
- **Adaptive Payloads** — smaller data on poor networks
- **Store & Forward Buffer** — pings saved during disconnect, synced on reconnect
- **ML ETA Prediction** — Random Forest model trained on 2000 historical trips
- **Path Smoothing** — bus trail interpolated between sparse GPS pings
- **Network Status UI** — Live / Offline / Syncing badge in real time

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
Open `frontend/index.html` in your browser.

---

## 📡 API Endpoints
| Endpoint | Description |
|----------|-------------|
| `GET /buses` | Live bus positions |
| `GET /buses?network=poor` | Minimal payload mode |
| `GET /routes` | All routes and stops |
| `GET /eta` | ML ETA prediction |
| `GET /sync` | Flush buffered offline pings |
| `GET /status` | Server health and buffer size |
| `GET /docs` | Interactive API documentation |

---

## 🧪 Testing
```bash
python test_integration.py
python simulate_network_drop.py
``` 
