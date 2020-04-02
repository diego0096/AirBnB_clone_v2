-- Create a database
-- Create hbnb_test_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create user:hbnb_test with password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Privilege to hbnb_test on database: hbnb_test_db
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Privilege to hbnb_test on database: performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
