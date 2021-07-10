DROP TABLE enrolments;
DROP TABLE lessons;
DROP TABLE adventurers;

CREATE TABLE adventurers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    adventurer_class VARCHAR(255)
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    lesson_name VARCHAR(255),
    recommended_for VARCHAR(255),
    lesson_description TEXT
);

CREATE TABLE enrolments (
    id SERIAL PRIMARY KEY,
    adventurer_id INT REFERENCES adventurers(id) ON DELETE CASCADE,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE
);