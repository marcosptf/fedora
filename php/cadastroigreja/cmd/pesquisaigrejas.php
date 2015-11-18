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
        <form  class="add-entry" action="../app/engine/command.php" method="post">
            <div class="flash">Pesquisa Igreja</div>
            <br/>
            <fieldset class="metanav">
                <div>
                    <label for="nameIgreja">Nome da Igreja</label>
                    <?php echo listaIgrejas(); ?>
                </div>
                <br/>
                <div>
                    <input name="command" type="hidden" value="pesquisaigreja" />
                    <button type="submit" class="pure-button pure-button-primary">buscar</button>
                    <a href="index.php"><button type="button" class="pure-button pure-button-primary">Voltar</button></a>
                </div>
            </fieldset>
        </form>
    </body>
    </div>
</html>

