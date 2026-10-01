# Agent Guidelines for Flask + Vue.js + SQLite App

## Project Structure
- `backend/`: Flask application with SQLAlchemy ORM
- `frontend/`: Vue.js (Vite) application

## Backend Setup
1. Install dependencies: `cd backend && pip install -r requirements.txt`
2. Set environment variables: ensure `.env` exists in backend directory (we have one)
3. Run development server: `cd backend && python run.py`
   - API available at http://localhost:5000/api
   - Database file: `backend/instance/app.db` (created automatically)

## Frontend Setup
1. Install dependencies: `cd frontend && npm install`
2. Run development server: `cd frontend && npm run dev`
   - Proxies `/api` requests to backend (http://localhost:5000) via Vite config
   - App available at http://localhost:5000 (Vite default port)

## Development Workflow
1. Start backend: `cd backend && python run.py`
2. In new terminal, start frontend: `cd frontend && npm run dev`
3. Frontend will automatically proxy API calls to backend

## Important Notes
- Backend creates SQLite tables on first run via `db.create_all()`
- Frontend uses Axios for HTTP requests; API base URL is relative (proxied by Vite)
- Environment variables for backend are loaded from `.env` in backend directory
- Do not commit `.env` or `instance/app.db` (add them to .gitignore)

## Verification
- Backend health check: `curl http://localhost:5000/api/items` (should return empty array initially)
- Frontend should display home page and fetch items from API
