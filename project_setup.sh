mkdir -p task-tracker/{backend/core/{models,controllers,utils},frontend/{css,js,assets/icons},database,tests} &&

touch task-tracker/backend/app.py &&
touch task-tracker/backend/core/__init__.py &&
touch task-tracker/backend/core/database.py &&

touch task-tracker/backend/core/models/__init__.py &&
touch task-tracker/backend/core/models/user.py &&
touch task-tracker/backend/core/models/task.py &&

touch task-tracker/backend/core/controllers/__init__.py &&
touch task-tracker/backend/core/controllers/auth_controller.py &&
touch task-tracker/backend/core/controllers/task_controller.py &&

touch task-tracker/backend/core/utils/__init__.py &&
touch task-tracker/backend/core/utils/security.py &&

touch task-tracker/frontend/index.html &&
touch task-tracker/frontend/dashboard.html &&
touch task-tracker/frontend/register.html &&
touch task-tracker/frontend/css/styles.css &&
touch task-tracker/frontend/js/scripts.js &&

touch task-tracker/database/schema.sql &&
touch task-tracker/database/seed_data.sql &&

touch task-tracker/tests/test_task.py &&

touch task-tracker/README.md &&
touch task-tracker/requirements.txt

