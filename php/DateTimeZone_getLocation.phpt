--TEST--
DateTimeZone::getLocation -- timezone_location_get — Returns location information for a timezone
public array DateTimeZone::getLocation ( void );
array timezone_location_get ( DateTimeZone $object )
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
$arrayDate = DateTimeZone::listAbbreviations();
foreach($arrayDate as $value){
    if(NULL != $value[0]['timezone_id']){
        $timeZone = new DateTimeZone($value[0]['timezone_id']);
        print_r($timeZone->getLocation());
        print_r(timezone_location_get($timeZone));
    }
}
?>
--EXPECTF--
