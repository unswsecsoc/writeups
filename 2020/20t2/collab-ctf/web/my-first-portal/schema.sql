CREATE TABLE users (
    username TEXT UNIQUE,
    password TEXT,
    level    TEXT   
);

INSERT INTO users (username, password, level) VALUES 
('bob', 'password123', 'user'),
('andy', 'i-have-a-better-password-than-bob', 'user'),
('megumin', 'i_love_kazuma', 'user'),
('flag', 'FLAG{2_pl81n_t3xt_0ffeNd3rS_T6RjMLt0y20}', 'user'),
('anna', 'some_generic_p3ssword_not', 'user');
