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
            print_r($timeZoneArray);
            #print("{$timeZoneArray['country_code']} \n");
        }
    }
}





