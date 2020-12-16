DROP TABLE bookings;
DROP TABLE lessons;
DROP TABLE members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)

);


CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
    capacity INT

);


CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE

);

