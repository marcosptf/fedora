<?php

require_once("../config/config.php");
require_once("../engine/functions.php");

//die("javascripter=>".var_dump(mysql_fetch_array($result)));
//die("javascripter=>".var_dump(mysql_num_rows($result)));
//die("javascripter=>".var_dump(($_POST)));
//die("javascripter=>".var_dump(($sqlInsert)));

$command=$_POST['command'];

if($command=="cadastraigreja"){
    cadastraIgreja($_POST);
    logmeMySql("cadastrou a igreja =>".print_r($_POST));
    header('Location:../../cmd/cadastraigreja.php');
}

if($command=="logon"){
    logmeMySql("usuario logando no sistema =>".print_r($_POST));
    if(logon($_POST)>0){
        header('Location:../../cmd/index.php');
    }else{
        header('Location:../../index.php');
    }
}

if($_GET['command']=="logout"){
    logmeMySql("usuario saindo do sistema =>".print_r($_POST));
    header('Location:index.php');
}

if($command=="cadastramembro"){
    cadastrandoMembro($_POST);
    logmeMySql("cadastrou a igreja =>".print_r($_POST));
    header('Location:../../cmd/cadastramembros.php');
}

if($command=="alteramembro"){
    alteraMembro($_POST);
    logmeMySql("cadastrou a igreja =>".print_r($_POST));
    header("Location:../../cmd/membros.php?id={$_POST['id']}");
}

if($command=="alteraigreja"){
    alteraIgreja($_POST);
    logmeMySql("cadastrou a igreja =>".print_r($_POST));
    header("Location:../../cmd/igreja.php?id={$_POST['id']}");
}

if($command=="pesquisaigreja"){
    $resp = buscaDadosIgreja($_POST);
    logmeMySql("cadastrou a igreja =>".print_r($_POST));
    header("Location:../../cmd/igreja.php?id={$resp['id']}");
}

