<?php
$arrayDate = DateTimeZone::listAbbreviations();
foreach($arrayDate as $value){ 
    if(NULL != $value[0]['timezone_id']){ 
        $timeZone = new DateTimeZone($value[0]['timezone_id']);
        print_r($timeZone->getLocation());
        print_r(timezone_location_get($timeZone));
    }   
}

