<?php
require_once("../app/config/config.php");
require_once("../app/engine/functions.php");
?>

<html>
    <head>
        <link rel="stylesheet" type="text/css" href="../app/css/estilos.css" />
    </head>
    <div class="page">
    <body>
        <form  class="add-entry"  action="pesquisamembros.php" method="post">
            <div class="flash">Pesquisa Membros</div>
            <br/>
            <fieldset class="metanav">
                <div>
                    <label for="nameIgreja">Nome do Membro</label>
                    <input id="nome" name="nome" type="text" placeholder="nome do membro">
                </div>
                
                <div>
                    <?php
                    if($_POST['command']=="pesquisamembro"){
                        print(buscaMembros($_POST['nome']));
                    }
                    ?>
                </div>
<!--                <div>
                    <label for="regional">Igreja</label>
                    <?php # echo listaIgrejas(); ?>
                </div>-->
                <br/>
                <div class="pure-controls">
                    <input name="command" type="hidden" value="pesquisamembro" />
                    <button type="submit" class="pure-button pure-button-primary">buscar</button>
                    <a href="index.php"><button type="button" class="pure-button pure-button-primary">Voltar</button></a>
                </div>
            </fieldset>
        </form>
    </body>
    <div/>
</html>

