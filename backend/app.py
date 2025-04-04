# backend/app.py
import sys # import system module to use system features 
import os # import operating system module for leting Python know where to look for modules 

# Let Python know where to look for modules (go up one folder)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import basic modules to create an HTTP server
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

# Import controllers that handle users and tasks
from core.controllers.auth_controller import AuthController
from core.controllers.task_controller import TaskController

PORT = 8000  # Port where the server will run (http://localhost:8000)

# Create a class that defines how to handle HTTP requests
class SimpleBackend(BaseHTTPRequestHandler):

    # This sets response headers (like content type and CORS policy)
    def _set_headers(self, content_type="text/html", status=200):
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")  # Allow frontend to connect
        self.end_headers()

    # Handle GET requests (when browser asks for pages or data)
    def do_GET(self):
        if self.path == "/":
            self.serve_html_file("frontend/index.html")
        elif self.path == "/register":
            self.serve_html_file("frontend/register.html")
        elif self.path == "/login":
            self.serve_html_file("frontend/login.html")
        elif self.path == "/dashboard":
            self.serve_html_file("frontend/dashboard.html")

        elif self.path == "/status":
            # Return a simple status to check if server is running
            self._set_headers("application/json")
            self.wfile.write(json.dumps({
                "status": "online",
                "message": "Task Tracker API is running"
            }).encode())

        elif self.path.startswith("/tasks"):
            # Extract username from the URL query string (?user=someone)
            from urllib.parse import urlparse, parse_qs
            query = parse_qs(urlparse(self.path).query)
            username = query.get("user", [None])[0]

            if not username:
                self._set_headers("application/json", 400)
                self.wfile.write(json.dumps({"error": "Missing username"}).encode())
                return

            # Check if user exists
            user = AuthController.find_user_by_username(username)
            if not user:
                self._set_headers("application/json", 404)
                self.wfile.write(json.dumps({"error": "User not found"}).encode())
                return

            # Get tasks for that user
            tasks = TaskController.get_tasks_by_user(user.get_id())
            tasks_data = [t.to_dict() for t in tasks]
            self._set_headers("application/json")
            self.wfile.write(json.dumps({"tasks": tasks_data}).encode())

        # allow my python application Serve CSS, JS, and image files to frontend
        elif self.path.startswith("/css/") or self.path.startswith("/js/") or self.path.startswith("/assets/icons/"):
            file_path = "frontend" + self.path
            try:
                with open(file_path, "rb") as f:
                    if self.path.endswith(".css"):
                        self._set_headers("text/css")
                    elif self.path.endswith(".js"):
                        self._set_headers("application/javascript")
                    elif self.path.endswith(".png"):
                        self._set_headers("image/png")
                    elif self.path.endswith(".jpg") or self.path.endswith(".jpeg"):
                        self._set_headers("image/jpeg")
                    elif self.path.endswith(".svg"):
                        self._set_headers("image/svg+xml")
                    elif self.path.endswith(".ico"):
                        self._set_headers("image/ico")
                    else:
                        self._set_headers("application/octet-stream")
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self._set_headers("text/plain", 404)
                self.wfile.write(b"404 - File not found")

    # allow my python project handle POST requests (like submitting forms: register, login, add task)
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode()
        parsed_data = parse_qs(post_data)

        if self.path == "/register":
            self.handle_register(parsed_data)
        elif self.path == "/login":
            self.handle_login(parsed_data)
        elif self.path == "/create-task":
            self.handle_create_task(parsed_data)
        elif self.path == "/update-task":
            self.handle_update_task(parsed_data)
        elif self.path == "/delete-task":
            self.handle_delete_task(parsed_data)
        else:
            self._set_headers("application/json", 404)
            self.wfile.write(json.dumps({"error": "Route not found"}).encode())

    # methode to register a new user
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
            self.wfile.write(json.dumps({
                "message": "User registered successfully.",
                "username": user.get_username()
            }).encode())
        else:
            self.wfile.write(json.dumps({"error": "User already exists."}).encode())

    # Log in as user who is existed before 
    def handle_login(self, data):
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

    # static methode to create a new task for a user
    def handle_create_task(self, data):
        username = data.get("username", [None])[0]
        title = data.get("title", [None])[0]
        description = data.get("description", [""])[0]
        due_date = data.get("due_date", [None])[0]
        priority = data.get("priority", ["Low"])[0]

        user = AuthController.find_user_by_username(username)
        if not user:
            self._set_headers("application/json", 404)
            self.wfile.write(json.dumps({"error": "User not found"}).encode())
            return

        TaskController.create_task(
            user_id=user.get_id(),
            title=title,
            description=description,
            due_date=due_date,
            priority=priority
        )

        self._set_headers("application/json")
        self.wfile.write(json.dumps({"message": "Task added!"}).encode())

    # a static methode to update an existing task
    def handle_update_task(self, data):
        username = data.get("username", [None])[0]
        task_id = data.get("task_id", [None])[0]
        title = data.get("title", [""])[0]
        description = data.get("description", [""])[0]
        priority = data.get("priority", ["Low"])[0]
        status = data.get("status", ["Pending"])[0]

        if not username or not task_id:
            self._set_headers("application/json", 400)
            self.wfile.write(json.dumps({"error": "Missing username or task ID"}).encode())
            return

        user = AuthController.find_user_by_username(username)
        if not user:
            self._set_headers("application/json", 404)
            self.wfile.write(json.dumps({"error": "User not found"}).encode())
            return

        updates = {
            "title": title,
            "description": description,
            "priority": priority,
            "status": status
        }

        success = TaskController.update_task(int(task_id), updates)

        self._set_headers("application/json")
        if success:
            self.wfile.write(json.dumps({"message": "Task updated successfully."}).encode())
        else:
            self.wfile.write(json.dumps({"error": "Task not found or update failed."}).encode())

    # methode to delete a task
    def handle_delete_task(self, data):
        task_id = data.get("task_id", [None])[0]

        if not task_id:
            self._set_headers("application/json", 400)
            self.wfile.write(json.dumps({"error": "Missing task ID"}).encode())
            return

        success = TaskController.delete_task(int(task_id))

        self._set_headers("application/json")
        if success:
            self.wfile.write(json.dumps({"message": "Task deleted successfully."}).encode())
        else:
            self.wfile.write(json.dumps({"error": "Task not found."}).encode())

    # methode to send an HTML file to the browser
    def serve_html_file(self, filepath):
        try:
            with open(filepath, "rb") as f:
                self._set_headers("text/html")
                self.wfile.write(f.read())
        except FileNotFoundError:
            self._set_headers("text/plain", 404)
            self.wfile.write(b"404 - File not found.")


# Start the server when running this file
if __name__ == "__main__":
    print(f"🚀 Server running on http://localhost:{PORT}")
    server_address = ("0.0.0.0", PORT) 
    httpd = HTTPServer(server_address, SimpleBackend)
    httpd.serve_forever()
