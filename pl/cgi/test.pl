#!/usr/bin/perl

# Testes de bibliotecas para Perl
# Autor: Sergio Abreu
# 2013-11-24

use DBI;
use strict;
use warnings;
use MySystem;
use MyDB;
use MyFile;
use MyForm;
use Data::Dumper;

startHeader();
 
# rpm 
  getConnection("<database>", "<user>", "<passwd>", "<host>");
 
# vagrant 
# getConnection("rpm_homolex", "root", "root" );

my @arr = dblist("Select * from cotacao_status", "id", 2);

my $res = $arr[0];
my $keys = $arr[1];

foreach ( @$keys){
  mpr( "$_ = ". $res->{$_}->{status} );
}

mpr( nl() . "Teste de arquivo: " . fileinfo('/home/vagrant/projetos/index.php') );
 
mpr( "Size: " . filesize('/home/vagrant/projetos/index.php') );
