/*  
criação das tabelas mysql
01/10/2014
marcosptf@yahoo.com.br
*/

/* database usado na aplicacao */
create database if not exists cadastro ;
use cadastro;

drop TABLE IF EXISTS `igrejas`;
drop TABLE IF EXISTS `membros`;
drop TABLE IF EXISTS `usuarios`;
drop TABLE IF EXISTS `param_cargo_ministerial`;
drop TABLE IF EXISTS `param_igreja_x_membro`;
drop TABLE IF EXISTS `param_perfil_x_usuario`;
drop TABLE IF EXISTS `param_perfil_usuario`;
drop TABLE IF EXISTS `param_perfil`;
drop TABLE IF EXISTS `logs`;


/* tabelas do sistema */
CREATE TABLE IF NOT EXISTS `igrejas` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `nome` varchar(250) NOT NULL,
    `endereco` varchar(250),
    `pais` varchar(250),
    `estado` varchar(250),
    `cidade` varchar(250),
    `bairro` varchar(250),
    `ministerio` varchar(250),
    `setor` varchar(250),
    `regional` varchar(250),
    `id_membro_resp_igreja` int(11),
PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `membros` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `id_igreja` int(11) NOT NULL,
    `nome` varchar(250) NOT NULL,
    `nome_pai` varchar(250),
    `nome_mae` varchar(250),
    `rg` varchar(15),
    `cpf` varchar(15),
    `idade` varchar(3),
    `data_nascimento` varchar(10),
    `data_batismo` varchar(10),
    `eh_batizado_es` int(1),
    `data_batismo_es` varchar(10),
    `naturalidade` varchar(250),
    `cargo_ministerial` varchar(2),
    `numero_registro` varchar(250),
    `foto` varchar(250),
    PRIMARY KEY (`id`)
);


CREATE TABLE IF NOT EXISTS `usuarios` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `usuario` varchar(25) NOT NULL,
    `senha` varchar(25) NOT NULL,
    PRIMARY KEY (`id`)
);
insert into usuarios
(usuario,senha)
values
('admin','administrador'),
('fabio','pedrinho2010');


/* tabelas de parametros */
CREATE TABLE IF NOT EXISTS `param_cargo_ministerial` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `descricao_cargo` varchar(250) NOT NULL,
    PRIMARY KEY (`id`)
);

insert into param_cargo_ministerial
(descricao_cargo)
values
('Reverendo.'),
('Missionario.'),
('Bispo.'),
('Co-Pastor.'),
('Pastor.'),
('Presbitero.'),
('Diacono.'),
('Coperador.'),
('Auxiliar.'),
('Maestro.'),
('Regente.'),
('Dirigente circulo de Oracao.'),
('Tesoureiro.'),
('Caseiro.'),
('Porteiro.'),
('Membro comum (sem cargo ministerial).'),
('Musico.');

CREATE TABLE IF NOT EXISTS `param_igreja_x_membro` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `id_igreja` int(11) NOT NULL,
    `id_membro` int(11) NOT NULL,
    PRIMARY KEY (`id`)
);


CREATE TABLE IF NOT EXISTS `param_perfil_x_usuario` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `id_usuario` varchar(11) NOT NULL,
    `id_perfil` varchar(11) NOT NULL,
    PRIMARY KEY (`id`)
);

insert into param_perfil_x_usuario
(id_usuario,id_perfil)
values
(1,1),
(2,2);

CREATE TABLE IF NOT EXISTS `param_perfil` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `descricao` varchar(250) NOT NULL,
    PRIMARY KEY (`id`)
);
insert into `param_perfil`
(descricao)
values
('admin'),
('usuario');

/* tabelas de log */
CREATE TABLE IF NOT EXISTS `logs` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `descricao` text NOT NULL,
    `datatime` timestamp default current_timestamp not null,
    PRIMARY KEY (`id`)
);


/* queryes  */
select membros.id,membros.id_igreja,nome,nome_pai,nome_mae,rg,cpf,idade,data_nascimento,data_batismo,eh_batizado_es,data_batismo_es,naturalidade,cargo_ministerial,numero_registro,foto,param_igreja_x_membro.id_igreja as igreja from membros inner join param_igreja_x_membro on param_igreja_x_membro.id_membro=membros.id where membros.id='1';


/* alteracao novos dados  */
alter table membros add estado_civil varchar(150);

CREATE TABLE IF NOT EXISTS `param_estado_civil` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `descricao` varchar(50) NOT NULL,
    PRIMARY KEY (`id`)
);
insert into `param_estado_civil`
(descricao)
values
('solteiro(a)'),
('divorciado(a)'),
('viuvo(a)'),
('casado(a)');