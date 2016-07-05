service mariadb start

mysql -uroot -p123456 sistema_de_espera


/* Esta query, cria um novo banco de dados para o sistema de espera. */
create database sistema_de_espera;

/* Esta query, faz o mysql selecionar o banco sistema_de_espera para as 
   proximas querys. */
use sistema_de_espera;

/* Nesta proxima query, é criado uma nova tabela no banco de dados 
   sistema_de_espera.
   Esta tabela é responsavel por gerar uma nova senha. */
create table painel (
 id integer primary key auto_increment,
 senha_prioridade integer default 0,
 senha_atendida   integer default 0,
 ultima_senha_atendida integer default 0
);

/* Esta query, lista todas as tabelas existentes no banco de dados
   sistema_de_espera. */
show tables;



----------------------------------------------------------------------------
truncate table painel;

insert into painel
(senha_prioridade, senha_atendida, ultima_senha_atendida)
values
(default, default, default);
insert into painel
(senha_prioridade, senha_atendida, ultima_senha_atendida)
values
(default, default, default);
insert into painel
(senha_prioridade, senha_atendida, ultima_senha_atendida)
values
(default, default, default);
insert into painel
(senha_prioridade, senha_atendida, ultima_senha_atendida)
values
(default, default, default);
insert into painel
(senha_prioridade, senha_atendida, ultima_senha_atendida)
values
(1, default, default);
insert into painel
(senha_prioridade, senha_atendida, ultima_senha_atendida)
values
(default, default, default);
insert into painel
(senha_prioridade, senha_atendida, ultima_senha_atendida)
values
(default, default, default);
insert into painel
(senha_prioridade, senha_atendida, ultima_senha_atendida)
values
(1, default, default);
insert into painel
(senha_prioridade, senha_atendida, ultima_senha_atendida)
values
(default, default, default);
insert into painel
(senha_prioridade, senha_atendida, ultima_senha_atendida)
values
(default, default, default);
select * from painel;




update   painel
set      ultima_senha_atendida = '0';

select 	 id 
from 	 painel 
where 	 senha_atendida = '0'
order by senha_prioridade desc,
         id asc
limit    1;

/* query para atualizar a proxima senha */
update   painel
set      ultima_senha_atendida = '1',
         senha_atendida = '1'
where    id = '';


select   id 
from     painel
where    ultima_senha_atendida = '1';


























