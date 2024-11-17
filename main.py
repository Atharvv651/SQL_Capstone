CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    stock_quantity INT,
    category VARCHAR(50)
);

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('John', 'Doe', 'Sales', 60000, '2020-01-15'),
('Jane', 'Smith', 'Marketing', 75000, '2018-07-20'),
('Alice', 'Johnson', 'Sales', 65000, '2019-03-30');

INSERT INTO products (name, price, stock_quantity, category) VALUES
('Laptop', 1200.00, 30, 'Electronics'),
('Smartphone', 800.00, 50, 'Electronics'),
('Tablet', 400.00, 70, 'Electronics'),
('Chair', 150.00, 100, 'Furniture');

INSERT INTO customers (first_name, last_name, city) VALUES
('Emily', 'Clark', 'New York'),
('Michael', 'Brown', 'Los Angeles'),
('Sarah', 'Wilson', 'New York');

INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2023-02-15', 1500.00),
(2, '2023-03-10', 800.00),
(3, '2023-01-05', 400.00);

SELECT * FROM employees;
SELECT * FROM products;
SELECT * FROM customers;
SELECT * FROM orders;

SELECT * FROM employees WHERE salary > 60000;
SELECT * FROM products WHERE category = 'Electronics';
SELECT * FROM customers WHERE city = 'New York';

SELECT * FROM employees ORDER BY salary DESC;
SELECT * FROM products ORDER BY price ASC;
SELECT * FROM customers ORDER BY city ASC;

SELECT AVG(salary) AS average_salary FROM employees;
SELECT MAX(price) AS max_price FROM products;
SELECT SUM(total_amount) AS total_revenue FROM orders;

SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department;
SELECT category, COUNT(*) AS product_count FROM products GROUP BY category;

SELECT e.first_name, e.last_name, o.total_amount FROM employees e
JOIN orders o ON e.id = o.customer_id;

SELECT e.first_name, e.last_name FROM employees e
LEFT JOIN orders o ON e.id = o.customer_id;

SELECT p.name, p.price FROM products p
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.total_amount > 1000);

SELECT DISTINCT city FROM customers;

SELECT COUNT(*) FROM employees;
SELECT COUNT(DISTINCT city) FROM customers;

SELECT * FROM orders WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';

SELECT * FROM employees LIMIT 2;

SELECT * FROM employees WHERE first_name LIKE 'J%';

DELETE FROM customers WHERE id = 2;

UPDATE products SET price = price * 1.1 WHERE category = 'Furniture';
