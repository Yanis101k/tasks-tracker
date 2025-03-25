-- -----------------------------------------
-- Insert sample users
-- Note: Passwords are hashed
-- -----------------------------------------
INSERT INTO users (username, email, password_hash)
VALUES 
    ('yanis_k', 'yanis@example.com', 'hashed_password_1'),
    ('sarah_d', 'sarah@example.com', 'hashed_password_2'),
    ('john_m', 'john@example.com', 'hashed_password_3');

-- -----------------------------------------
-- Insert sample tasks for user #1 (yanis_k)
-- -----------------------------------------
INSERT INTO tasks (user_id, title, description, due_date, priority, status, tags)
VALUES 
    (1, 'Finish database schema', 'Complete and review schema.sql and seed_data.sql', '2025-03-25', 'High', 'In Progress', 'school,urgent'),
    (1, 'Buy groceries', 'Get milk, bread, and eggs', '2025-03-26', 'Medium', 'Pending', 'personal'),
    (1, 'Workout', '30-minute run + pushups', '2025-03-24', 'Low', 'Completed', 'health'),

-- -----------------------------------------
-- Insert sample tasks for user #2 (sarah_d)
-- -----------------------------------------
    (2, 'Study Python OOP', 'Watch 2 tutorials and write notes', '2025-03-27', 'High', 'Pending', 'learning,python'),
    (2, 'Clean the house', 'Living room, kitchen, and bathroom', '2025-03-26', 'Medium', 'Pending', 'home'),

-- -----------------------------------------
-- Insert sample tasks for user #3 (john_m)
-- -----------------------------------------
    (3, 'Read tech blog', 'Explore GeeksforGeeks software quality article', '2025-03-24', 'Low', 'Completed', 'reading,tech');
