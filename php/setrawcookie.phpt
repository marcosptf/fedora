--TEST--
bool setrawcookie ( string $name [, string $value [, int $expire = 0 [, string $path [, string $domain [, bool $secure = false [, bool $httponly = false ]]]]]] );
--CREDITS--
marcosptf - <marcosptf@yahoo.com.br>
--FILE--
<?php
$cookieName = "cookie1";
$cookieValue = "value1";
setcookie("Test", "123456", time()+3600, "/~rasmus/", "example.com", 1);
var_dump(headers_list());


?>
--EXPECT--
