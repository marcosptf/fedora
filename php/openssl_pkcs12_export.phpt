--TEST--
bool openssl_pkcs12_export ( mixed $x509 , string &$out , mixed $priv_key , string $pass [, array $args ] );
--CREDITS--
marcosptf - <marcosptf@yahoo.com.br>
--SKIPIF--
<?php if (!extension_loaded("openssl")) print "skip";
if (OPENSSL_VERSION_NUMBER < 0x10000000) die("skip Output requires OpenSSL 1.0");
if (!@openssl_pkey_new()) die("skip cannot create private key"); 
?>
--FILE--
<?php
/*  bool openssl_pkcs12_export ( mixed $x509 , string &$out , mixed $priv_key , string $pass [, array $args ] ); */
openssl_pkcs12_export ( mixed $x509 , string &$out , mixed $priv_key , string $pass [, array $args ] );
openssl_pkcs12_export ( mixed $x509 , string &$out , mixed $priv_key , string $pass);

$pemFile = "bug37820cert.pem";
$keyFile = "bug37820key.pem";
$privkeyFilePem = "file://" . dirname(__FILE__) . "/{$keyFile}";
$privkeyDirPem = __DIR__ . "/{$pemFile}";
$passPhrase = "JavaIsBetterThanPython:-)";
$cert = openssl_x509_read(file_get_contents($privkeyDirPem));
$privkey = openssl_pkey_get_private($privkeyFilePem);
var_dump($privkey);
var_dump(openssl_pkcs12_export($cert, $out, $privkey, $passphrase));
var_dump($out);




?>
--EXPECT--
