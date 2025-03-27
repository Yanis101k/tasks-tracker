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
        """
        Send standard HTTP response headers.
        """
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        """
        Handle GET requests (for now, just a health check).
        """
        if self.path == "/":
            self._set_headers()
            self.wfile.write(b"<h1> Server is running!</h1>")
        else:
            self._set_headers("application/json", 404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())

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
        else:
            self._set_headers("application/json", 404)
            self.wfile.write(json.dumps({"error": "Route not found"}).encode())

    def handle_register(self, data):
        """
        Handle user registration from /register POST form.
        """
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
            self.wfile.write(json.dumps({"message": "User registered successfully."}).encode())
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


# Run the server
if __name__ == "__main__":
    print(f"🚀 Server running on http://localhost:{PORT}")
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, SimpleBackend)
    httpd.serve_forever()
