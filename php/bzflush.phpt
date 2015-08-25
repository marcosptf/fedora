--TEST--
int bzflush ( resource $bz );
--CREDITS--
marcosptf - <marcosptf@yahoo.com.br>
--SKIPIF--
<?php
<?php if (!extension_loaded("bz2")) print "skip"; ?>
?>
--FILE--
<?php
$handle = gzopen(__DIR__ . '/bzflush.test.bz2', 'r');

$bz = bzopen($handle, 'w');

if (bzflush($bz)) {
    print("OK");

} else {
    print("open bzip2 file has failed!");
}

bzclose($bz);
?>
--EXPECT--
OK
