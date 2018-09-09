#
#source perl repository and dependences:
#https://metacpan.org/pod/Net::MySQL
#https://metacpan.org/pod/IO::Socket
#https://metacpan.org/pod/Digest::SHA1
#
use Net::MySQL;
 
my $mysql = Net::MySQL->new(
    hostname => '127.0.0.1:3306',
    database => 'rpm_controlex2',
    user     => 'root',
    password => ''
);
 
# INSERT example
#$mysql->query(q{
#    INSERT INTO tablename (first, next) VALUES ('Hello', 'World')
#});
#printf "Affected row: %d\n", $mysql->get_affected_rows_length;
 
# SLECT example
$mysql->query(q{select * from rpmuser});
my $record_set = $mysql->create_record_iterator;
while (my $record = $record_set->each) {
    printf "First column: %s Next column: %s\n",
        $record->[0], $record->[1];
}
$mysql->close;

