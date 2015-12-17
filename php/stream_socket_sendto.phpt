--TEST--
int stream_socket_sendto ( resource $socket , string $data [, int $flags = 0 [, string $address ]] );
--CREDITS--
marcosptf - <marcosptf@yahoo.com.br> - #phparty7 - @phpsp - novatec/2015 - sao paulo - br
--SKIPIF--
<?php
if (phpversion() < "5.3.0") {
  die('SKIP php version so lower.');
}
?>
--FILE--
<?php
$serverUri = "tcp://127.0.0.1:31854";
$sock = stream_socket_server($serverUri, $errno, $errstr);

if (is_resource($sock)) {
  fwrite($sock, "Normal data transmit.");
  var_dump(stream_socket_sendto($sock, "Out of Band data."));
  var_dump(stream_socket_sendto($sock, "Out of Band data.", STREAM_OOB));
  var_dump(stream_socket_sendto($sock, "Out of Band data.", STREAM_OOB, $serverUri));
} else {
  die("Test stream_socket_enable_crypto has failed; Unable to connect: {$errstr} ({$errno})");
}
?>
--CLEAN--
fclose($sock);
--EXPECT--
001+ Notice: fwrite(): send of 21 bytes failed with errno=32 Broken pipe in /home/travis/build/php/php-src/ext/standard/tests/streams/stream_socket_sendto.php on line 6

003+ Warning: stream_socket_sendto(): Broken pipe

004+  in /home/travis/build/php/php-src/ext/standard/tests/streams/stream_socket_sendto.php on line 7

005+ int(-1)

006+ 

007+ Warning: stream_socket_sendto(): Broken pipe

008+  in /home/travis/build/php/php-src/ext/standard/tests/streams/stream_socket_sendto.php on line 8

009+ int(-1)

010+ 

011+ Warning: stream_socket_sendto(): php_network_getaddresses: getaddrinfo failed: Name or service not known in /home/travis/build/php/php-src/ext/standard/tests/streams/stream_socket_sendto.php on line 9

012+ 

013+ Warning: stream_socket_sendto(): Failed to resolve `tcp': php_network_getaddresses: getaddrinfo failed: Name or service not known in /home/travis/build/php/php-src/ext/standard/tests/streams/stream_socket_sendto.php on line 9

014+ 

015+ Warning: stream_socket_sendto(): Failed to parse `tcp://127.0.0.1:31854' into a valid network address in /home/travis/build/php/php-src/ext/standard/tests/streams/stream_socket_sendto.php on line 9


016+ bool(false)




Notice: fwrite(): send of %d bytes failed with errno=%d Broken pipe in %s on line %d
Warning: stream_socket_sendto(): Broken pipe
in %s on line %d
int(%i)
