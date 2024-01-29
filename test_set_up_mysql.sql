CREATE DATABASE IF NOT EXISTS test_bookswap_dev_db;
CREATE USER IF NOT EXISTS 'test_bookswap_dev'@'localhost' IDENTIFIED BY 'test_bookswap_dev_pwd';
GRANT ALL PRIVILEGES ON `test_bookswap_dev_db`.* TO 'test_bookswap_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'test_bookswap_dev'@'localhost';
FLUSH PRIVILEGES;