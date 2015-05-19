<?php
error_reporting(E_ALL);


mysql_connect("127.0.0.1","root");
$respQuery = mysql_query("select id,xmlsend from test.xmlsend where xmlsent='0';");
while($mysqlFetch = mysql_fetch_array($respQuery)){

print("iniciando envio... \n");
print("id=>".$mysqlFetch['id']."\n");
print("xml=>".$mysqlFetch['xmlsend']."\n\n");

$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,"http://endpoint.com?wsdl");
curl_setopt($ch,CURLOPT_HEADER, TRUE);
curl_setopt($ch,CURLOPT_NOBODY, TRUE); // remove body
curl_setopt($ch,CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($ch,CURLOPT_USERPWD, 'IG:08igIGnEt24x');
curl_setopt($ch,CURLOPT_POST,true);
curl_setopt($ch,CURLOPT_POSTFIELDS,$mysqlFetch['xmlsend']);
$head = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
mysql_query("update test.xmlsend set xmlsent='1' where id='".$mysqlFetch['id']."'");
print("resp=>".$httpCode." =>".$head);
print("envio finalizado \n\n\n\n\n");
curl_close($ch);

sleep(0.5);
}

