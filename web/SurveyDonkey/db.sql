create table users(id int(4) unsigned auto_increment primary key,
uname varchar(50) not null unique key, password varchar(300) not null);

create table survey(id int(4) unsigned auto_increment primary key, uid int(4), sname varchar(500));

create table questions (id int(6) unsigned auto_increment primary key,sid int(4) not null, question varchar(500) not null);

create table options (id int(8) unsigned auto_increment primary key,qid int(6) not null, optiontitle varchar(500) not null, count int(6));

insert into users (uname, password) values('user1', 'pass1');
insert into users (uname, password) values('user2', 'pass2');