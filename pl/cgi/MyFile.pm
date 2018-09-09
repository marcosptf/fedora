#!/usr/bin/perl

# File functions for Perl
# Author: Sergio Abreu
# 2013-11-23

package MyFile;
require Exporter;
require MySystem;
use strict;
use warnings;
 
our @ISA = qw(Exporter);
our @EXPORT = qw(fileinfo filesize fileread filewrite);
our @EXPORT_OK = qw(fileinfo filesize fileread filewrite);

sub fileinfo{

	my $file = $_[0];
	my (@description, $size);
	if (-e $file)
	{
	   push @description, 'binary' if (-B _);
	   push @description, 'a socket' if (-S _);
	   push @description, 'a text file' if (-T _);
	   push @description, 'a block special file' if (-b _);
	   push @description, 'a character special file' if (-c _);
	   push @description, 'a directory' if (-d _);
	   push @description, 'executable' if (-x _);
	   push @description, (($size = -s _)) ? "$size bytes" : 'empty';
	   
	   return "$file is " . join(', ',@description) . "\n";

	} else {
	
             if( isHttp() ){
	       
	          return "<span style='color:red'>File $file doesn't exist.</span>" . nl();
	          
	       } else {
	       
	          return "[ Error: File $file doesn't exist. ]" . nl();
	       }	    	       
	
	}
 
}

sub filesize{

      my( $file, $size);

	$file = $_[0];
      $size = 0;

	if (-e $file)
	{
	   ($size = -s _) ;
	}

   return $size + 0;
}

sub fileread{
  
     my $file = $_[0];

     if( -e $file){

   	  open( ARQ, $file);
	     my $content = <ARQ>;
	     close( ARQ );
	     
	     return $content;
     
     } else {
     
  	       if( isHttp() ){
	       
	          return "<span style='color:red'>File $file doesn't exist.</span>" . nl();
	          
	       } else {
	       
	          return "[ Error: File $file doesn't exist. ]" . nl();
	       }	     
     }
 
}

sub filewrite{
    # reserved
}

1;