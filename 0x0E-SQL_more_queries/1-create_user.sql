-- creates the MySQL server user user_0d_1.
-- user_0d_1 should have all privileges on your MySQL server
-- The user_0d_1 password should be set to user_0d_1_pwd
-- To make a new user -> CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
-- To provide the user with all privileges -> GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = PASSWORD('user_0d_1_pwd');
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
