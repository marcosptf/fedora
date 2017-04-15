/* Esta query, cria um novo banco de dados para o sistema de espera. */
create database sistema_de_contatos;

/* Esta query, faz o mysql selecionar o banco sistema_de_espera para as 
   proximas querys. */
use sistema_de_contatos;

/* Nesta proxima query, é criado uma nova tabela no banco de dados 
   sistema_de_espera.
   Esta tabela é responsavel por gerar uma nova senha. */
create table contatos (
  id integer primary key auto_increment,
  nome varchar(250) not null,
  email varchar(50) default null,
  whatsapp varchar(12) default null,
  facebook varchar(50) default null,
  twitter varchar(50) default null,
  website varchar(50) default null,
  endereco varchar(250) default null,
  bairro varchar(50) default null,
  cidade varchar(50) default null,
  estado varchar(50) default null
);

/* Esta query, lista todas as tabelas existentes no banco de dados
   sistema_de_espera. */
show tables;
show create table contatos;
select * from contatos;
