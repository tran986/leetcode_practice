CREATE TABLE Employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
);

INSERT INTO Employee (name, salary)
VALUES
('Nia', 80000),
('Alex', 95000),
('Sam', 70000);

SELECT * FROM Employee;