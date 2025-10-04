-- seed.sql
-- Insert sample data into CrediAI database

-- Sample Users
INSERT INTO users (username, email, hashed_password, full_name)
VALUES
('alice', 'alice@example.com', 'hashedpassword1', 'Alice Johnson'),
('bob', 'bob@example.com', 'hashedpassword2', 'Bob Smith'),
('charlie', 'charlie@example.com', 'hashedpassword3', 'Charlie Lee');

-- Sample Loans
INSERT INTO loans (user_id, loan_amount, income, credit_score, loan_purpose, status)
VALUES
(1, 5000, 60000, 720, 'personal', 'approved'),
(2, 15000, 80000, 680, 'education', 'pending'),
(3, 7000, 50000, 650, 'car', 'denied');

-- Sample Predictions
INSERT INTO predictions (user_id, loan_id, prediction, confidence)
VALUES
(1, 1, 'approved', 0.95),
(2, 2, 'pending', 0.70),
(3, 3, 'denied', 0.85);