create table users(id serial  PRIMARY KEY NOT NULL ,
uname char(50) NOT NULL, password char(300) NOT NULL);

create table survey(id serial PRIMARY KEY , uid INT, sname char(500));

create table questions (id serial PRIMARY KEY ,sid INT NOT NULL, question char(500) NOT NULL);

create table options (id serial PRIMARY KEY ,qid INT NOT NULL, optiontitle char(500) NOT NULL, count INT;

insert INTo users (uname, password) values('user1', 'pass1');
insert INTo users (uname, password) values('user2', 'pass2');
