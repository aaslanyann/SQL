CREATE TABLE users_finances(
    id INT AUTO_INCREMENT PRIMARY KEY,
    salary INT,
    bonus INT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)