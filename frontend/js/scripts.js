const loginForm = document.getElementById("loginForm");
const messageDiv = document.getElementById("message");

loginForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const formData = new FormData(loginForm);
  const data = new URLSearchParams(formData);

  try {
    const response = await fetch("http://localhost:8000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: data
    });

    const result = await response.json();
    console.log("📦 Server response:", result);

    if (response.ok && result.message) {
      messageDiv.textContent = "✅ " + result.message;
      messageDiv.style.color = "green";

      // ✅ Store session and redirect to dashboard
      localStorage.setItem("username", result.username);
      window.location.href = "/dashboard";
    } else {
      messageDiv.textContent = "❌ " + (result.error || "Login failed.");
      messageDiv.style.color = "red";
    }

  } catch (error) {
    messageDiv.textContent = "❌ Network error: " + error.message;
    messageDiv.style.color = "red";
  }
});

const registerForm = document.getElementById("registerForm");

registerForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const formData = new FormData(registerForm);
  const data = new URLSearchParams(formData);

  try {
    const response = await fetch("http://localhost:8000/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: data
    });

    const result = await response.json();
    console.log("📦 Server response:", result);

    if (response.ok && result.message && result.username) {
      // ✅ Store session and redirect
      localStorage.setItem("username", result.username);
      window.location.href = "/dashboard";
    } else {
      messageDiv.textContent = "❌ " + (result.error || "Registration failed.");
      messageDiv.style.color = "red";
    }

  } catch (error) {
    messageDiv.textContent = "❌ Network error: " + error.message;
    messageDiv.style.color = "red";
  }
});

const username = localStorage.getItem("username");
    const taskList = document.getElementById("taskList");
    const taskForm = document.getElementById("taskForm");
   

    // If user is not logged in, redirect to login
    if (!username) {
      window.location.href = "/login";
    }

    // Display logged-in username
    document.getElementById("username").textContent = username;

    // Fetch and display all tasks for the current user
    async function loadTasks() {
      try {
        const res = await fetch(`http://localhost:8000/tasks?user=${username}`);
        const result = await res.json();
        taskList.innerHTML = "";

        // Render each task with edit/delete buttons
        result.tasks.forEach(task => {
          const li = document.createElement("li");

          li.innerHTML = `
            <strong>${task.title}</strong> (${task.priority}) - ${task.status}
            <button onclick="showUpdateForm(${task.id})">✏️ Edit</button>
            <button onclick="deleteTask(${task.id})">❌ Delete</button>

            <!-- Inline task edit form -->
            <div id="edit-form-${task.id}" style="display:none; margin-top:10px;">
              <input type="text" id="edit-title-${task.id}" value="${task.title}">
              <input type="text" id="edit-description-${task.id}" value="${task.description}">
              <select id="edit-priority-${task.id}">
                <option ${task.priority === "Low" ? "selected" : ""}>Low</option>
                <option ${task.priority === "Medium" ? "selected" : ""}>Medium</option>
                <option ${task.priority === "High" ? "selected" : ""}>High</option>
              </select>
              <select id="edit-status-${task.id}">
                <option ${task.status === "Pending" ? "selected" : ""}>Pending</option>
                <option ${task.status === "In Progress" ? "selected" : ""}>In Progress</option>
                <option ${task.status === "Completed" ? "selected" : ""}>Completed</option>
              </select>
              <button onclick="updateTask(${task.id})">💾 Save</button>
            </div>
          `;
          taskList.appendChild(li);
        });

      } catch (err) {
        taskList.innerHTML = "<li>❌ Failed to load tasks.</li>";
      }
    }

    // Handle task creation
    taskForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const formData = new FormData(taskForm);
      formData.append("username", username);

      try {
        const res = await fetch("http://localhost:8000/create-task", {
          method: "POST",
          body: new URLSearchParams(formData),
          headers: { "Content-Type": "application/x-www-form-urlencoded" }
        });

        const result = await res.json();
        if (res.ok && result.message) {
          messageDiv.textContent = "✅ " + result.message;
          messageDiv.style.color = "green";
          taskForm.reset();
          loadTasks();
        } else {
          messageDiv.textContent = "❌ " + (result.error || "Could not add task.");
          messageDiv.style.color = "red";
        }

      } catch (err) {
        messageDiv.textContent = "❌ Network error: " + err.message;
        messageDiv.style.color = "red";
      }
    });

    // Show inline form to update a task
    function showUpdateForm(taskId) {
      document.getElementById(`edit-form-${taskId}`).style.display = "block";
    }

    // Submit task update to the backend
    async function updateTask(taskId) {
      const title = document.getElementById(`edit-title-${taskId}`).value;
      const description = document.getElementById(`edit-description-${taskId}`).value;
      const priority = document.getElementById(`edit-priority-${taskId}`).value;
      const status = document.getElementById(`edit-status-${taskId}`).value;

      const updateData = new URLSearchParams();
      updateData.append("username", username);
      updateData.append("task_id", taskId);
      updateData.append("title", title);
      updateData.append("description", description);
      updateData.append("priority", priority);
      updateData.append("status", status);

      try {
        const res = await fetch("http://localhost:8000/update-task", {
          method: "POST",
          body: updateData,
          headers: { "Content-Type": "application/x-www-form-urlencoded" }
        });

        const result = await res.json();
        if (res.ok && result.message) {
          messageDiv.textContent = "✅ " + result.message;
          messageDiv.style.color = "green";
          loadTasks();
        } else {
          messageDiv.textContent = "❌ " + (result.error || "Update failed.");
          messageDiv.style.color = "red";
        }

      } catch (err) {
        messageDiv.textContent = "❌ Network error: " + err.message;
        messageDiv.style.color = "red";
      }
    }

    // Send request to delete a task
    async function deleteTask(taskId) {
      const confirmDelete = confirm("Are you sure you want to delete this task?");
      if (!confirmDelete) return;

      const data = new URLSearchParams();
      data.append("task_id", taskId);

      try {
        const res = await fetch("http://localhost:8000/delete-task", {
          method: "POST",
          body: data,
          headers: { "Content-Type": "application/x-www-form-urlencoded" }
        });

        const result = await res.json();
        if (res.ok && result.message) {
          messageDiv.textContent = "🗑️ " + result.message;
          messageDiv.style.color = "green";
          loadTasks();
        } else {
          messageDiv.textContent = "❌ " + (result.error || "Delete failed.");
          messageDiv.style.color = "red";
        }

      } catch (err) {
        messageDiv.textContent = "❌ Network error: " + err.message;
        messageDiv.style.color = "red";
      }
    }

    // Handle logout
    document.getElementById("logoutBtn").addEventListener("click", () => {
      localStorage.removeItem("username");
      window.location.href = "/login";
    });

    // Load tasks when page opens
    loadTasks();

