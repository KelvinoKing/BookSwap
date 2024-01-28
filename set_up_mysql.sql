CREATE DATABASE IF NOT EXISTS bookswap_dev_db;
CREATE USER IF NOT EXISTS 'bookswap_dev'@'localhost' IDENTIFIED BY 'bookswap_dev_pwd';
GRANT ALL PRIVILEGES ON `bookswap_dev_db`.* TO 'bookswap_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'bookswap_dev'@'localhost';
FLUSH PRIVILEGES;