CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS game (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    price NUMERIC(10,2) NOT NULL,
    description TEXT,
    genre TEXT,
    categories TEXT,
    hardware_requirements TEXT,
    released_at TIMESTAMPTZ NOT NULL,

    embedding VECTOR(2000)
);

ALTER TABLE game
ALTER COLUMN embedding TYPE vector(2048)
USING embedding::vector(2048);
