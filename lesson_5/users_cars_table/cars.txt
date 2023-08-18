CREATE TABLE cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car VARCHAR(30),
    model VARCHAR(30),
    car_year VARCHAR(10),
    car_number VARCHAR(20),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);