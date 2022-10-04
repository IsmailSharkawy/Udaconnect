CREATE EXTENSION postgis;

CREATE TABLE location (
    id SERIAL PRIMARY KEY,
    person_id INT NOT NULL,
    coordinate GEOMETRY NOT NULL,
    creation_time TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE INDEX coordinate_idx ON location (coordinate);
CREATE INDEX creation_time_idx ON location (creation_time);

-- TRUNCATE TABLE person RESTART IDENTITY CASCADE;
-- TRUNCATE TABLE location RESTART IDENTITY CASCADE;
