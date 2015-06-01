#!/usr/bin/perl

#to program perl, is used use strict to develop in strict mode, the script will stop each time that the code is wrong mode;
use strict;
#the warnings dont stop the execution of code, but will send message of mistakes on the fly;
use warnings;

#to declare variables on strict mode
my $animal = "camelo";
my $answer = 42; 

#to concat variable, is used commas ','
print("my animal is $animal and his age is ",$answer);

#arrays
my @animals = ("camels","llama","dogs","cats");
my @numbers = (23,34,65,234,677,23,34);
my @sort = sort @numbers;
my @backwards = reverse @numbers;
my %fruitColors = (); 

#print arrays
print("\n\n",$animals[0],"\n");
print($numbers[4],"\n");

#print the last number of array range
print("\n",$numbers[$#numbers]);

#err compilation fail,try again
#print("\n",$sort);
#print("\n",$backwards);

#hashes
my %fruitColor = ( 
apple => 'red',
strawberry => 'strong red',
watermellow => 'green',
banana => 'yellow',
);
print("\n",$fruitColor{"apple"});

#ways to get list os keys/values pairs
my @fruits = keys %fruitColors;
my @colors = values %fruitColors;

#kinds of variables in perl
my %variables = { 
    scalar => {
                description => "single item",
                sigil => '$' 
        },  
    array  => {
                description => "ordered list of items",
                sigil => '@' 
        },  
    hash   => {
                description => "key/value pairs",
                sigil => '%'
        }
};

#to print it =>
#fail
#print("\n", $variables->{'scalar'}->{'description'});


print("\n");

