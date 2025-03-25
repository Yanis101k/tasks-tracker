-- --------------------------------------------------
-- remove existing tables in our database ( for development resets only )
-- Ensures a clean slate before creating new tables 
-- --------------------------------------------------
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;

-- --------------------------------------------------
-- Create `users` table
-- Stores basic user account information
-- --------------------------------------------------
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,    -- Unique user ID (auto-incremented)
    username VARCHAR(50) NOT NULL,                 -- Username (e.g., "YanisK")
    email VARCHAR(100) NOT NULL UNIQUE,            -- Email address (must be unique)
    password_hash VARCHAR(255) NOT NULL,           -- Hashed password for security
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP  -- Timestamp when account was created
);

-- --------------------------------------------------
-- Create `tasks` table
-- Stores all tasks created by users 
-- --------------------------------------------------
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,             -- Unique task ID
    user_id INT NOT NULL,                          -- Foreign key: links to the user who created the task
    title VARCHAR(100) NOT NULL,                   -- Short task title (e.g., "Study databases")
    description TEXT,                              -- Optional longer description
    due_date DATE,                                 -- Optional deadline date
    priority ENUM('Low', 'Medium', 'High')         -- Task priority level
        DEFAULT 'Low',                             -- Default is 'Low' if not specified
    status ENUM('Pending', 'In Progress', 'Completed')  
        DEFAULT 'Pending',                         -- Task status (default is 'Pending')
    tags VARCHAR(255),                             -- Optional tags (e.g., "school,urgent")
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when task was created
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP  -- Auto-update when task is modified
        ON UPDATE CURRENT_TIMESTAMP,
    -- Foreign key constraint for user-task relationship
    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE                          -- If user is deleted, delete all their tasks too
);
