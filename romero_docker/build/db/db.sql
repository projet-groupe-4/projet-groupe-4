CREATE USER IF NOT EXISTS admin@'%' IDENTIFIED BY 'admin';
SET PASSWORD FOR admin@'%' = PASSWORD('admin');
CREATE DATABASE IF NOT EXISTS presentation;
GRANT ALL ON *.* TO admin@'%';
-- WITH GRANT OPTION;
USE presentation;
SOURCE /var/lib/mysql/articles.sql;
FLUSH PRIVILEGES;
