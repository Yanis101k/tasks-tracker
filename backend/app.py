# backend/app.py
import sys
import os

# Add the root directory to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

# Optional: for later integration
from core.controllers.auth_controller import AuthController
from core.controllers.task_controller import TaskController

PORT = 8000

class SimpleBackend(BaseHTTPRequestHandler):
    def _set_headers(self, content_type="text/html", status=200):
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")  # ✅ Allow requests from frontend
        self.end_headers()

    
    def do_GET(self):
            """
            Handle GET requests for frontend pages and API routes.
            """
            if self.path == "/":
                self._set_headers("text/html")
                self.wfile.write(b"<h1> Task Tracker Server is Running</h1><p>Visit /register or /login</p>")

            elif self.path == "/register":
                self.serve_html_file("frontend/register.html")

            elif self.path == "/login":
                self.serve_html_file("frontend/login.html")
            
            elif self.path == "/dashboard":
                 self.serve_html_file("frontend/dashboard.html")
 
            elif self.path == "/status":
                self._set_headers("application/json")
                self.wfile.write(json.dumps({
                    "status": "online",
                    "message": "Task Tracker API is running"
                }).encode())
            elif self.path.startswith("/tasks"):
                from urllib.parse import urlparse, parse_qs
                query = parse_qs(urlparse(self.path).query)
                username = query.get("user", [None])[0]

                from core.controllers.auth_controller import AuthController
                from core.controllers.task_controller import TaskController

                if not username:
                    self._set_headers("application/json", 400)
                    self.wfile.write(json.dumps({"error": "Missing username"}).encode())
                    return

                user = AuthController.find_user_by_username(username)
                if not user:
                    self._set_headers("application/json", 404)
                    self.wfile.write(json.dumps({"error": "User not found"}).encode())
                    return

                tasks = TaskController.get_tasks_by_user(user.get_id())
                tasks_data = [t.to_dict() for t in tasks]
                self._set_headers("application/json")
                self.wfile.write(json.dumps({"tasks": tasks_data}).encode())


    
    def do_POST(self):
        """
        Handle POST requests (e.g., /register, /login, /create-task).
        """
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode()
        parsed_data = parse_qs(post_data)  # Handles form-encoded data

        if self.path == "/register":
            self.handle_register(parsed_data)
        elif self.path == "/login":
            self.handle_login(parsed_data)
        elif self.path == "/create-task":
             self.handle_create_task(parsed_data)
        else:
            self._set_headers("application/json", 404)
            self.wfile.write(json.dumps({"error": "Route not found"}).encode())

    def handle_register(self, data):
        username = data.get("username", [None])[0]
        email = data.get("email", [None])[0]
        password = data.get("password", [None])[0]

        if not username or not email or not password:
            self._set_headers("application/json", 400)
            self.wfile.write(json.dumps({"error": "Missing fields"}).encode())
            return

        user = AuthController.register_user(username, email, password)

        self._set_headers("application/json")
        if user:
            # ✅ Include username in the response for auto-login
            self.wfile.write(json.dumps({
                "message": "User registered successfully.",
                "username": user.get_username()
            }).encode())
        else:
            self.wfile.write(json.dumps({"error": "User already exists."}).encode())


    def handle_login(self, data):
        """
        Handle user login from /login POST form.
        """
        email = data.get("email", [None])[0]
        password = data.get("password", [None])[0]

        if not email or not password:
            self._set_headers("application/json", 400)
            self.wfile.write(json.dumps({"error": "Missing email or password"}).encode())
            return

        user = AuthController.login_user(email, password)
        self._set_headers("application/json")
        if user:
            self.wfile.write(json.dumps({
                "message": "Login successful",
                "username": user.get_username()
            }).encode())
        else:
            self.wfile.write(json.dumps({"error": "Invalid credentials"}).encode())
    def handle_create_task(self, data):
        username = data.get("username", [None])[0]
        title = data.get("title", [None])[0]
        description = data.get("description", [""])[0]
        due_date = data.get("due_date", [None])[0]
        priority = data.get("priority", ["Low"])[0]

        from core.controllers.auth_controller import AuthController
        from core.controllers.task_controller import TaskController

        user = AuthController.find_user_by_username(username)
        if not user:
            self._set_headers("application/json", 404)
            self.wfile.write(json.dumps({"error": "User not found"}).encode())
            return

        task = TaskController.create_task(
            user_id=user.get_id(),
            title=title,
            description=description,
            due_date=due_date,
            priority=priority
        )

        self._set_headers("application/json")
        self.wfile.write(json.dumps({"message": "Task added!"}).encode())

    def serve_html_file(self, filepath):
        """
        Serve an HTML file from the frontend directory.
        """
        try:
            with open(filepath, "rb") as f:
                self._set_headers("text/html")
                self.wfile.write(f.read())
        except FileNotFoundError:
            self._set_headers("text/plain", 404)
            self.wfile.write(b"404 - File not found.")


# Run the server
if __name__ == "__main__":
    print(f"🚀 Server running on http://localhost:{PORT}")
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, SimpleBackend)
    httpd.serve_forever()
