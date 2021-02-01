CREATE DATABASE comma_db;
USE comma_db;

CREATE TABLE IF NOT EXISTS board (
    id int not null AUTO_INCREMENT,
    name varchar(64) not null,
    created timestamp default NOW(),
    primary key (id)
);

CREATE TABLE IF NOT EXISTS board_article (
    id int not null AUTO_INCREMENT,
    title varchar(64) not null,
    content text,
    board_id int not null,
    created timestamp default NOW(),
    primary key (id),
    foreign key (board_id) references board(id)
);

CREATE TABLE IF NOT EXISTS user (
    id int not null AUTO_INCREMENT,
    fullname varchar(32) not null,
    email varchar(32) not null,
    password longtext not null,
    joined timestamp default NOW(),
    primary key (id)
);


INSERT INTO board (name) values ('고양이1');
INSERT INTO board (name) values ('고양이2');
INSERT INTO board (name) values ('고양이3');

INSERT INTO board_article (title, content, board_id) VALUES ('고양이1', '고양이1', 1);
INSERT INTO board_article (title, content, board_id) VALUES ('고양이2', '고양이2', 2);
INSERT INTO board_article (title, content, board_id) VALUES ('고양이3', '고양이3', 3);

INSERT INTO user (fullname, email, password) VALUES ('집사1', '집사1@elice.com', '집사1');
INSERT INTO user (fullname, email, password) VALUES ('집사2', '집사2@elice.com', '집사2');
INSERT INTO user (fullname, email, password) VALUES ('집사3', '집사3@elice.com', '집사3');