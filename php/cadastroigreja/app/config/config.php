<?php
error_reporting(0);
//error_reporting(E_ALL);

$host = '127.0.0.1';
$username = 'root';
$password = '123456';
$database = 'cadastro';

$cn = mysql_connect($host, $username, $password);
mysql_select_db($database);
