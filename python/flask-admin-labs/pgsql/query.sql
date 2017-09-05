
-- lista todas as tabelas 
SELECT * FROM pg_catalog.pg_tables

-- tabela de usuario do flask admin
create table usuario (
  id serial PRIMARY KEY, 
  first_name VARCHAR(100), 
  last_name VARCHAR(100), 
  login VARCHAR(80), 
  email VARCHAR(120), 
  password VARCHAR(64), 
  UNIQUE (login)
);


