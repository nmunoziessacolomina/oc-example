# Agent Guidelines for Flask + Vue.js + SQLite App

## Project Structure
- `backend/`: Flask application with SQLAlchemy ORM
- `frontend/`: Vue.js (Vite) application

## Backend Setup
1. Set up virtual environment: 
   - If not exists: `cd backend && python -m venv .venv`
   - Activate: `source .venv/bin/activate` (or `. .venv/bin/activate`)
   - Install dependencies: `pip install -r requirements.txt`
2. Set environment variables: ensure `.env` exists in backend directory (we have one)
3. Run development server: `cd backend && source .venv/bin/activate && python run.py` (or use the venv python directly: `.venv/bin/python run.py`)
   - API available at http://<host-ip>:5000/api (where <host-ip> is the server's IP address, e.g., 192.168.1.45)
   - Database file: `backend/instance/app.db` (created automatically)

## Frontend Setup
1. Install dependencies: `cd frontend && npm install`
2. Run development server: `cd frontend && npm run dev`
   - Proxies `/api` requests to backend (http://localhost:5000) via Vite config
   - App available at http://localhost:5000 (Vite default port)

## Development Workflow
1. Start backend: `cd backend && source .venv/bin/activate && python run.py` (or use venv python directly: `.venv/bin/python run.py`)
2. In new terminal, start frontend: `cd frontend && npm run dev`
3. Frontend will automatically proxy API calls to backend

## Important Notes
- Backend creates SQLite tables on first run via `db.create_all()`
- Frontend uses Axios for HTTP requests; API base URL is relative (proxied by Vite)
- Environment variables for backend are loaded from `.env` in backend directory (we set `FLASK_HOST=0.0.0.0` to listen on all IPs)
- Backend virtual environment is located at `backend/.venv` (do not commit)
- Do not commit `.env`, `instance/app.db`, or `backend/.venv` (add them to .gitignore)

## Verification
- Backend health check: `curl http://<host-ip>:5000/api/items` (should return empty array initially, where <host-ip> is the server's IP address)
- Frontend should display home page and fetch items from API

## Feature: Posts CRUD with Mock Data
This feature implements CRUD operations for posts using mock data in the Flask backend.
- **Backend changes**:
  - `app/models.py`: Added Post model
  - `app/routes.py`: Added REST API endpoints for posts (GET, POST, PUT, DELETE)
  - `app/config.py`: Updated configuration for the feature
  - `app/__init__.py`: Updated to initialize the feature
  - `run.py`: Updated to run the application
  - `.env`: Added environment variables for the feature
- **Note**: The frontend integration is not included in this feature; the mock data is served by the backend API.
