-- Seed initial users
INSERT INTO users (full_name, email, hashed_password, is_admin)
VALUES
('Admin User', 'admin@credi.ai', '$2b$12$examplehashedpassword', TRUE),
('Test User', 'user@credi.ai', '$2b$12$examplehashedpassword', FALSE);

-- Seed initial loans
INSERT INTO loans (user_id, amount, status)
VALUES
(2, 5000.0, 'pending'),
(2, 12000.0, 'pending');