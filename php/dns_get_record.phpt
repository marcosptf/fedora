--TEST--
array dns_get_record ( string $hostname [, int $type = DNS_ANY [, array &$authns [, array &$addtl [, bool &$raw = false ]]]] );
--CREDITS--
marcosptf - <marcosptf@yahoo.com.br> - #phparty7 - @phpsp - novatec/2015 - sao paulo - br
--FILE--
<?php
$hostname = "yahoo.com";

var_dump(dns_get_record($hostname));
?>
--CLEAN--
<?php
//unset($hostname);
?>
--EXPECTF--
array(%d) {
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["txt"]=>
    string(%d) "%s"
    ["entries"]=>
    array(%d) {
      [%d]=>
      string(%d) "%s"
    }
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["mname"]=>
    string(%d) "%s"
    ["rname"]=>
    string(%d) "%s"
    ["serial"]=>
    int(%d)
    ["refresh"]=>
    int(%d)
    ["retry"]=>
    int(%d)
    ["expire"]=>
    int(%d)
    ["minimum-ttl"]=>
    int(%d)
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["pri"]=>
    int(%d)
    ["target"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["pri"]=>
    int(%d)
    ["target"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["pri"]=>
    int(%d)
    ["target"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["ipv6"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%s) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["ipv6"]=>
    string(%d) "%s"
  }
  [7]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["ipv6"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["ip"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["ip"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["ip"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["target"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["target"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%d"
    ["target"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["target"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["target"]=>
    string(%d) "%s"
  }
  [%d]=>
  array(%d) {
    ["host"]=>
    string(%d) "yahoo.com"
    ["class"]=>
    string(%d) "%s"
    ["ttl"]=>
    int(%d)
    ["type"]=>
    string(%d) "%s"
    ["target"]=>
    string(%d) "%s"
  }
}
