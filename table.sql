CREATE EXTENSION IF NOT EXISTS vector;

CREATE TYPE schedule_type AS ENUM ('lecture', 'practice');

CREATE TABLE IF NOT EXISTS schedule (
    id SERIAL PRIMARY KEY,
    subject_name VARCHAR(255) NOT NULL,
    starting_at TIMESTAMP NOT NULL,
    teacher VARCHAR(255) NOT NULL,
    cabinet INT NOT NULL,
    type schedule_type NOT NULL
);

-- add a vector columns

ALTER TABLE schedule
ADD COLUMN IF NOT EXISTS embedding vector(2048);
