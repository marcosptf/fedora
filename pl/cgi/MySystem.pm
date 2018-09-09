#!/usr/bin/perl

# Basic functions for Perl
# Author: Sergio Abreu
# 2013-11-23

package MySystem;
require Exporter;
use strict;
use warnings;

our @ISA = qw(Exporter);
our @EXPORT = qw( startHeader nl showEnv isHttp isTerminal mpr);
our @EXPORT_OK = qw( startHeader nl showEnv isHttp isTerminal mpr);

sub startHeader{
  print "Content-type: text/html \n\n";
}

sub showEnv {
    for my $k ( keys(%ENV)){
        print "$k = $ENV{$k}" . nl();
    }
}
    
sub mpr {
   print $_[0] . nl();
}

sub isHttp {
  return defined( $ENV{SERVER_ADDR} );
}

sub isTerminal {
  return defined( $ENV{SHELL} );
}

sub nl {
  if( isHttp()){
      return "<br />\n";
   }
 else
   {
     return  "\n" ;
   }
}

1;