CREATE DATABASE library;

USE library;

CREATE TABLE books (
    Bno INT PRIMARY KEY,
    title VARCHAR(255),
    is_issued BOOLEAN DEFAULT FALSE
);

CREATE TABLE members (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE issues (
    book_id INT,
    member_id INT,
    FOREIGN KEY (book_id) REFERENCES books(Bno),
    FOREIGN KEY (member_id) REFERENCES members(id)
);
