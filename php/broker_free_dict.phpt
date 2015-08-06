--TEST--
enchant_broker_free() function
--SKIPIF--
<?php 
if(!extension_loaded('enchant')) die('skip, enchant not loader');
?>
--FILE--
<?php
$broker = enchant_broker_init();
if (is_resource($broker)) {
    echo("OK\n");
    if (enchant_broker_free($broker)) {
        echo("OK\n");
    } else { 
        echo("broker free failed\n");
    }
}  else {
	echo("init failed\n");
}
echo("OK\n");
?>
--EXPECT--
OK
OK
OK
