CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO users (name, email)
VALUES
('Alice', 'alice@example.com'),
('Borys', 'borys@example.com');
