DROP TABLE IF EXISTS employees;

CREATE TABLE employees(
		worker_id INT PRIMARY KEY,
		first_name VARCHAR(50) NOT NULL,
		last_name VARCHAR(50) NOT NULL,
		salary DECIMAL NOT NULL,
		joining_date DATE,
		department VARCHAR(50));

CREATE TABLE bonus(
		worker_ref_id INT PRIMARY KEY,
		bonus_date DATE,
		bonus_amount INT);

CREATE TABLE title(
		worker_ref_id INT PRIMARY KEY,
		worker_title VARCHAR(50),
		affected_from DATE);



INSERT INTO employees (first_name, last_name, salary, joining_date, department) VALUES ('Rick', 'Smith', '100000', '2021-02-20 09:00:00', 'HR');
INSERT INTO employees (first_name, last_name, salary, joining_date, department) VALUES ('Sam', 'Williams', '80000', '2021-06-11 09:00:00', 'Admin');
INSERT INTO employees (first_name, last_name, salary, joining_date, department) VALUES ('John', 'Brown', '300000', '2021-02-20 09:00:00', 'HR');
INSERT INTO employees (first_name, last_name, salary, joining_date, department) VALUES ('Amy', 'Jones', '500000', '2021-02-20 09:00:00', 'Admin');
INSERT INTO employees (first_name, last_name, salary, joining_date, department) VALUES ('Sean', 'Garcia', '500000', '2021-06-11 09:00:00', 'Admin');
INSERT INTO employees (first_name, last_name, salary, joining_date, department) VALUES ('Ryan', 'Miller', '200000', '2021-06-11 09:00:00', 'Account');
INSERT INTO employees (first_name, last_name, salary, joining_date, department) VALUES ('Patty', 'Davis', '75000', '2021-01-20 09:00:00', 'Account');
INSERT INTO employees (first_name, last_name, salary, joining_date, department) VALUES ('Monica', 'Rodriquez', '90000', '2021-04-11 09:00:00', 'Admin');




SELECT first_name, last_name FROM employees WHERE salary BETWEEN 50000 AND 100000;

SELECT department, count(*) FROM employees GROUP BY department ORDER BY count(*) DESC;

SELECT worker_ref_id FROM employees INTERSECT SELECT worker_ref_id FROM bonus; 

SELECT first_name, last_name FROM ( SELECT *, ROW_NUMBER() OVER (ORDER BY salary DESC) T FROM employees) WHERE T = 5; 
