--TEST--
mixed openssl_pkcs7_verify ( string $filename , int $flags [, string $outfilename [, array $cainfo [, string $extracerts [, string $content ]]]] );
--CREDITS--
marcosptf - <marcosptf@yahoo.com.br>
--SKIPIF--
<?php 
if (!extension_loaded("openssl")) print "skip";
if (OPENSSL_VERSION_NUMBER < 0x10000000) die("skip Output requires OpenSSL 1.0");
?>
--FILE--
<?php
$emlFile = "test_sample_message.eml";
$caFile = "san-ca.pem";
$fileEml = "file://" . dirname(__FILE__) . "/{$emlFile}";
$fileEml = __DIR__ . DIRECTORY_SEPARATOR . "/{$emlFile}";
$fileCa = dirname(__FILE__) . "/{$emlFile}";
$pemFile = "bug37820cert.pem";
$extraCerts = __DIR__ . "/{$pemFile}";

var_dump(openssl_pkcs7_verify($fileEml, PKCS7_TEXT));
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_BINARY));
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_NOINTERN));
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_NOVERIFY));
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_NOCHAIN));
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_NOCERTS));
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_NOATTR));
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_DETACHED));
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_NOSIGS));
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_TEXT, $outFileName1));
var_dump($outFileName1);


var_dump(openssl_pkcs7_verify($fileEml, PKCS7_TEXT, $outFileName2, null));
var_dump($outFileName2);
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_TEXT, $outFileName3, array()));
var_dump($outFileName3);
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_TEXT, $outFileName4, array($fileCa)));
var_dump($outFileName4);
var_dump(openssl_pkcs7_verify($fileEml, PKCS7_TEXT, $outFileName5, array($fileCa), $extraCerts));
var_dump($outFileName5);

openssl_pkcs7_verify($fileEml, int $flags [, string $outfilename [, array $cainfo [, string $extracerts [, string $content ]]]] );


openssl_pkcs7_verify($fileEml, int $flags [, string $outfilename [, array $cainfo [, string $extracerts [, string $content ]]]] );

?>
--EXPECT--
