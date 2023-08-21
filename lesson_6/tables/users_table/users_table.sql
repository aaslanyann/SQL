CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	email VARCHAR(30) UNIQUE,
	age int,
	country VARCHAR(20) CHECK (country IN ('Armenia', 'Russia', 'Georgia'))
);
