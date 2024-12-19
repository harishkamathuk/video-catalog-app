CREATE TABLE media (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT UNIQUE NOT NULL,
    file_size INTEGER,
    media_type_id INTEGER,
    duration REAL,
    resolution TEXT,
    codec TEXT,
    bit_rate INTEGER,
    date_created TEXT,
    date_modified TEXT,
    hash TEXT UNIQUE,
    FOREIGN KEY (media_type_id) REFERENCES media_type (id)
);
