CREATE DATABASE k17coins;

CREATE TABLE `k17coins`.`users` (
    `id` INTEGER AUTO_INCREMENT,
    `username` VARCHAR(255),
    `subacc` INTEGER,
    `money` FLOAT,
    `password` TEXT,
    PRIMARY KEY (`id`)
);

CREATE TABLE `k17coins`.`goods` (
    `id` INTEGER AUTO_INCREMENT,
    `name` VARCHAR(255),
    `content` TEXT,
    `price` FLOAT,
    PRIMARY KEY (`id`)
);

CREATE TABLE `k17coins`.`user_good` (
    `user` INTEGER,
    `good` INTEGER
);

INSERT INTO `k17coins`.`goods` (`name`, `content`, `price`) VALUES('why Earth is flat', 'ask adamt', 1);
INSERT INTO `k17coins`.`goods` (`name`, `content`, `price`) VALUES('how to git gud', 'have you tried being a better hacker', 10);
INSERT INTO `k17coins`.`goods` (`name`, `content`, `price`) VALUES('flag', 'FLAG{C0NCURRENCY15hArd}', 666);

CREATE USER 'k17coins'@'%' IDENTIFIED BY 'SECURE_K17COINS_DB_PASSWD';
GRANT SELECT, INSERT, UPDATE ON k17coins.users TO 'k17coins'@'%';
GRANT SELECT ON k17coins.goods TO 'k17coins'@'%';
GRANT SELECT, INSERT ON k17coins.user_good TO 'k17coins'@'%';
FLUSH PRIVILEGES;
