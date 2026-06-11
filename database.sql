-- Run this in phpMyAdmin or MySQL CLI
CREATE DATABASE IF NOT EXISTS internship_db;
USE internship_db;

CREATE TABLE IF NOT EXISTS students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  phone VARCHAR(15) NOT NULL,
  college VARCHAR(150) NOT NULL,
  department VARCHAR(100) NOT NULL,
  year_of_study VARCHAR(20) NOT NULL,
  internship_domain VARCHAR(100) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
