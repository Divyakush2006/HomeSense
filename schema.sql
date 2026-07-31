-- HomeSense task store
-- Apply with:  mysql -u root -p < schema.sql

CREATE DATABASE IF NOT EXISTS todo;
USE todo;

CREATE TABLE IF NOT EXISTS data (
    work    VARCHAR(255) NOT NULL,
    dateow  DATE         NOT NULL,
    status  VARCHAR(10)  NOT NULL DEFAULT 'Not Done',
    INDEX idx_dateow (dateow)
);
