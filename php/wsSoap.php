<?php

ini_set("soap.wsdl_cache_enabled", "0");
print "<pre>";

$cliente = new SoapClient('http://127.0.0.1/?wsdl' , array('trace' => 1));

$fieldsInteratividade = array('auth' => array('login' => 'usuario', 'password' => '123456'),
            'msisdn' => 5511920130607,
            'keyword' => 'compra');


try {
    print_r($cliente->interatividade($fieldsInteratividade));
} catch (Exception $exc) {
    echo $exc->getMessage();
}
die;
