CREATE TABLE user_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
	weight VARCHAR(20),
	height VARCHAR(20),
	eyes_color VARCHAR(20),
	user_id INT,
	FOREIGN KEY (user_id) REFERENCES users(id)
);