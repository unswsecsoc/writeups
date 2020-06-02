CREATE TABLE phonebooks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    user_id TEXT NOT NULL,
    created INT NOT NULL
);

CREATE TABLE phonenumbers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pbid INT NOT NULL,
    phonenumber TEXT NOT NULL,
    numberowner TEXT,

    FOREIGN KEY(pbid) REFERENCES phonebooks(id)
);

CREATE TABLE messages (
    pbid INT NOT NULL,
    message TEXT NOT NULL
);
