#!/usr/bin/perl

# RPM database Perl connector
# Author: Sergio Abreu
# 2013-11-23

package MyDB;
require Exporter;
use DBI;
use strict;
use warnings; 
use Data::Dumper;

our @ISA = qw(Exporter);
our @EXPORT = qw(getConnection dblist discon dbinfo dbrow);
our @EXPORT_OK = qw(getConnection dblist discon dbinfom dbrow);

my ($DSN, $cp, $cp_key, $ord_cp, $ord_type, $user, $pass, @keys, %ha, @arr); 
my ($sql, $item, $dbh, $sth, $res, $row, $key, $value, $index, @hash, $banco, $n, $host);

sub getConnection{
  
  $n = scalar(@_); #conta os argumentos.

  $banco = $_[0];
  $user  = $_[1];
  $pass  = $_[2];
  $host  = ($n eq 3 ? "127.0.0.1" : $_[3]);

  $DSN  = "DBI:mysql:$banco;host=$host";

  $dbh = DBI->connect( $DSN, $user, $pass, {RaiseError=>1} ) 
       || die "Could not connect to database: $DBI::errstr";

  return $dbh;
}


sub dbinfo{

	$sql = $_[0];

	$sth = $dbh->prepare( $sql);
	$sth->execute();

	my @res = $sth->fetchrow_arrayref(); 

	$sth->finish;

  	return $res[0][0];

}

sub dbrow{

	$n = scalar(@_); #conta os argumentos.

	$sql = $_[0];
	$cp_key = $_[1];
	$ord_type = ($n == 2 ? 0 : $_[2]); 
	$ord_cp = ($n <= 3 ? $cp_key : $_[3]);

	$sth = $dbh->prepare( $sql);
	$sth->execute();

	$res = $sth->fetchall_hashref( $cp_key); 

	$sth->finish;

	if( $ord_type > 0){
 
		if( $ord_type == 1){ # Léxico

		   @keys = sort{ $res->{$a}->{$ord_cp} cmp $res->{$b}->{$ord_cp} } keys(%$res);

		} elsif ( $ord_type == 2){ # Numérico:
 
		   @keys = sort{ $res->{$a}->{$ord_cp} <=> $res->{$b}->{$ord_cp} } keys(%$res); 

		}
            
	} else {

          @keys = keys(%$res);
        }

        if( scalar(@keys) == 1){

          return $res->{ $keys[0]};
 
        } else {
        
	  return ($res, \@keys);
       }

}

sub dblist{

	$n = scalar(@_); #conta os argumentos.

	$sql = $_[0];
	$cp_key = $_[1];
	$ord_type = ($n == 2 ? 0 : $_[2]); 
	$ord_cp = ($n <= 3 ? $cp_key : $_[3]);

	$sth = $dbh->prepare( $sql);
	$sth->execute();

	$res = $sth->fetchall_hashref( $cp_key); 

	$sth->finish;

	if( $ord_type > 0){
 
		if( $ord_type == 1){ # Léxico

		   @keys = sort{ $res->{$a}->{$ord_cp} cmp $res->{$b}->{$ord_cp} } keys(%$res);

		} elsif ( $ord_type == 2){ # Numérico:
 
		   @keys = sort{ $res->{$a}->{$ord_cp} <=> $res->{$b}->{$ord_cp} } keys(%$res); 
		}
            
	} else {

          @keys = keys(%$res);
        }

        
	return ($res, \@keys);

}

sub discon{
  $dbh->disconnect();
}
 
1;