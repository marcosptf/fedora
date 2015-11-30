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
<?php
$arrayDate = DateTimeZone::listAbbreviations();
$countryCode = array("??");
$count = 0;

foreach($arrayDate as $value){

    if(NULL != $value[0]['timezone_id']){
        $timeZone = new DateTimeZone($value[0]['timezone_id']);
        $timeZoneArray = $timeZone->getLocation();

        if((!in_array($timeZoneArray['country_code'], $countryCode)) && (NULL != $timeZoneArray['country_code']) && ("" != $timeZoneArray['country_code'])) {
            array_push($countryCode, $timeZoneArray['country_code']);
            var_dump(timezone_location_get($timeZone));
            var_dump($timeZoneArray);
            #print("{$timeZoneArray['country_code']} \n");
        }   
    }   
}


?>
--EXPECTF--
