#make with perl version =>
#[marcosptf@localhost html]$ perl --version
#
#This is perl 5, version 22, subversion 4 (v5.22.4) built for x86_64-linux-thread-multi
#(with 61 registered patches, see perl -V for more detail)
#Copyright 1987-2017, Larry Wall
##Perl may be copied only under the terms of either the Artistic License or the
#GNU General Public License, which may be found in the Perl 5 source kit.
#Complete documentation for Perl, including FAQ lists, should be found on
#this system using "man perl" or "perldoc perl".  If you have access to the
#Internet, point your browser at http://www.perl.org/, the Perl Home Page.
#

use strict;
use warnings;
use WWW::Curl::Easy;

my $curl = WWW::Curl::Easy->new;

#aqui vamos importar um modulo perl para se conectar ao mysql
#e trazer a url que vamos chamar na fila e finalizar a carga
$curl->setopt(CURLOPT_HEADER,1);
$curl->setopt(CURLOPT_URL, 'http://127.0.0.1/cargaitemfornecedor/cargaitem?perl_load_data_carga_item_fornecedor=true');

# A filehandle, reference to a scalar or reference to a typeglob can be used here.
my $response_body;
$curl->setopt(CURLOPT_WRITEDATA,\$response_body);

# Starts the actual request
my $retcode = $curl->perform;

# Looking at the results...
if ($retcode == 0) {
        print("Transfer went ok\n");
        my $response_code = $curl->getinfo(CURLINFO_HTTP_CODE);
        # judge result and next action based on $response_code
        print("Received response: $response_body\n");
} else {
        # Error code, type of error, error message
        print("An error happened: $retcode ".$curl->strerror($retcode)." ".$curl->errbuf."\n");
}


