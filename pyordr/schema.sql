CREATE TABLE IF NOT EXISTS task (
       id             INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
       date_added     INTEGER NOT NULL,
       date_completed INTEGER,
       name_          TEXT    NOT NULL UNIQUE,
       description    TEXT    NOT NULL DEFAULT '',
       state_         INTEGER NOT NULL DEFAULT 0
);
