CREATE TABLE user_mobiles(
    id INT AUTO_INCREMENT PRIMARY KEY,
    phone_number VARCHAR(30),
    operator VARCHAR(30),
    mobile_country VARCHAR(30),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)