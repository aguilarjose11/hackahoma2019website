drop table if exists keychain;
drop table if exists entrepreuners;
create table keychain (
  id integer primary key autoincrement,
  username text not null,
  password text not null,
  first text not null,
  last text not null,
  email text not null,
  phone text not null
);

create table entrepreuners (
  id integer primary key autoincrement,
  projectname text not null,
  projectdesc text not null,
  user text not null

);

insert into keychain (username, password, first, last, email, phone) values ('admin','admin', 'Jhonny', 'Test', 'example@email.com', '1234567890');
