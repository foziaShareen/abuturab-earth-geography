# 1️⃣ Swagger (Swagger UI)

Swagger is a tool for API documentation and testing.

What it does

Automatically shows all your API endpoints

Displays:

URL paths

HTTP methods (GET, POST, etc.)

Parameters

Request body

Response schemas

Lets you test APIs directly in the browser (no Postman needed)
In FastAPI

FastAPI automatically generates Swagger UI.

📍 Default URL:

<http://127.0.0.1:8000/docs>

```
@app.get("/countries")
def get_countries():
    return ["Pakistan", "India", "China"]
```
Swagger will show:

GET /countries

A Try it out button

Response preview

✅ Swagger is for humans (developers)
❌ It does not run your server
2️⃣ Uvicorn

Uvicorn is an ASGI web server.

What it does

Runs your FastAPI app

Listens on a port (like 8000)

Handles HTTP requests

Sends responses back to clients (browser, Node.js, mobile app, etc.)

Why FastAPI needs Uvicorn

FastAPI is just Python code, it cannot run by itself.
Uvicorn is the engine that runs it.
uvicorn main:app --reload
📍 Server runs at:

http://127.0.0.1:8000
🧠 Easy analogy

FastAPI → Recipe 🍲

Uvicorn → Stove 🔥 (cooks/runs it)

Swagger → Menu + tasting counter 📋😄
ASGI Web Server (Simple Explanation)

ASGI stands for
👉 Asynchronous Server Gateway Interface

An ASGI web server is a server that can run async Python web applications.
Why ASGI exists

Old Python servers (like WSGI) could handle:

Only one request at a time per worker

Only synchronous code

Modern apps need:

WebSockets

Real-time chat

Long-running connections

Async APIs

👉 ASGI solves this
What an ASGI Web Server does

An ASGI web server:

Receives HTTP / WebSocket requests

Passes them to your ASGI app (FastAPI, Starlette, Django async)

Handles async & sync code

Sends responses back to the client

Examples of ASGI servers:

Uvicorn

Hypercorn

Daphne
ASGI vs WSGI (important)
Feature	WSGI	ASGI
Async support	❌ No	✅ Yes
WebSockets	❌ No	✅ Yes
HTTP/2	❌ No	✅ Yes
Background tasks	Limited	Excellent
Used by	Flask, Django (old)	FastAPI, Starlette
