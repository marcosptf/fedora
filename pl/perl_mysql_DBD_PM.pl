#!/usr/bin/perl
#
#source perl module
#https://metacpan.org/pod/DBD::mysql
#
#to install dependences:
#1.#https://metacpan.org/pod/DBD::mysql  => download tar
#tar zxvf ~/Downloads/DBD-mysql-4.047.tar.gz
#
#2.change perl module name:
#cp -rfv DBD-mysql-4.047/ DBI/ => to root directory on perl code
#
#3. run perl mysql code on same directory above
#perl perl_mysql_script.pl
#
#
#doc to install on server completly:
#https://metacpan.org/pod/distribution/DBD-mysql/lib/DBD/mysql/INSTALL.pod
#
 
use strict;
use warnings;
use DBI;
 
# Connect to the database.
my $dbh = DBI->connect("DBI:mysql:database=rpm_controlex2;host=localhost",
                       "root", "",
                       {'RaiseError' => 1});

print("connect perl-mysql=> okey");

# Drop table 'foo'. This may fail, if 'foo' doesn't exist
# Thus we put an eval around it.
#eval { $dbh->do("DROP TABLE foo") };
#print "Dropping foo failed: $@\n" if $@;
 
# Create a new table 'foo'. This must not fail, thus we don't
# catch errors.
#$dbh->do("CREATE TABLE foo (id INTEGER, name VARCHAR(20))");
 
# INSERT some data into 'foo'. We are using $dbh->quote() for
# quoting the name.
#$dbh->do("INSERT INTO foo VALUES (1, " . $dbh->quote("Tim") . ")");
 
# same thing, but using placeholders (recommended!)
#$dbh->do("INSERT INTO foo VALUES (?, ?)", undef, 2, "Jochen");
 
# now retrieve data from the table.
my $sth = $dbh->prepare("select user_id, user_name from rpmuser");
$sth->execute();
while (my $ref = $sth->fetchrow_hashref()) {
  print "Found a row: id = $ref->{'user_id'}, name = $ref->{'user_name'}\n";
}
$sth->finish();
 
# Disconnect from the database.
$dbh->disconnect();


