CREATE DATABASE IF NOT EXISTS forum_db;

USE forum_db;

CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tresc TEXT,
    godzina DATETIME,
    ip VARCHAR(45)
);
