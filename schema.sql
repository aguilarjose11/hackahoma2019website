drop table if exists keychain;
drop table if exists entrepreuners;
create table keychain (
  id integer primary key autoincrement,
  username text not null,
  password text not null
);

create table entrepreuners (
  id integer primary key autoincrement,
  projectname text not null,
  projectdesc text not null,

)
