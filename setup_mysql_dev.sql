-- Create a database
-- Create hbnb_dev_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user:hbnb_dev with password 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Privilege to hbnb_dev for database: hbnb_dev_db
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Privilege to hbnb_dev on database: performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
