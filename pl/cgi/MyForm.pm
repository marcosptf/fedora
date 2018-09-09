#!/usr/bin/perl

# Form functions for Perl
# Author: Sergio Abreu
# 2013-11-23

package MyForm;
require Exporter;
use strict;
use warnings; 
use Data::Dumper;

our @ISA = qw(Exporter);
our @EXPORT = qw( getParamString getRequestParams);
our @EXPORT_OK = qw( getParamString getRequestParams);
 
my( $str, $pair, @pairs, $name, $value, %hash, $buf, $n );
 
sub getRequestParams{
 
  $n = scalar(@_);
  $str = ( $n > 0 ? $_[0] : getParamString());
   
  if( $str gt ""){
   
    @pairs = split( /&/, $str);
  
  	foreach $pair( @pairs){
	    ($name, $value) = split(/=/, $pair);
	     $name =~ tr/+/\ /;
	     $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	     $value =~ tr/+/\ /;
	     $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	     $hash{$name} = $value;
	  }
	   
	  return \%hash;
  
  } else {
  
    return undef;
  }
   
}

sub getParamString{

 if( defined $ENV{'REQUEST_METHOD'}){

	 if( $ENV{'REQUEST_METHOD'} eq 'POST'){
	   read(STDIN, $buf, $ENV{'CONTENT_LENGTH'});
	
	 } else {
	  $buf = $ENV{'QUERY_STRING'};
	 }
	 
    return $buf;
  } 
   else {
    return "";
   }
}

1;