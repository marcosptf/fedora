<?php
require_once("../app/config/config.php");
require_once("../app/engine/functions.php");

$respDados = buscaDadosMembros($_GET['id']);
?>

<html>
    <head>
        <link rel="stylesheet" type="text/css" href="../app/css/estilos.css" />
    </head>
    <div class="page">
        <body>
            <form action="../app/engine/command.php" method="post">
                <div class="flash">Pesquisa Membros</div>
                <br/>
                <fieldset class="metanav">
                    <table class="add-entry">
                        <tr>
                            <td>
                                <label for="nameIgreja">Nome do Membro</label>
                            </td>
                            <td>
                                <input id="nome" name="nome" type="text" value="<?= $respDados['nome'] ?>">
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="nome_pai">Nome do Pai</label>
                            </td>
                            <td>
                                <input id="nome_pai" name="nome_pai" type="text"  value="<?= $respDados['nome_pai'] ?>" />
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="nome_mae">Nome mae</label>
                            </td>
                            <td>
                                <input id="nome_mae" name="nome_mae" type="text"  value="<?= $respDados['nome_mae'] ?>" />
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="rg">RG</label>
                            </td>
                            <td>
                                <input id="rg" name="rg" type="text"  value="<?= $respDados['rg'] ?>" />
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="cpf">CPF</label>
                            </td>
                            <td>
                                <input id="cpf" name="cpf" type="text"  value="<?= $respDados['cpf'] ?>" />
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="idade">idade</label>
                            </td>
                            <td>
                                <input id="idade" name="idade" type="text"  value="<?= $respDados['idade'] ?>" />
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="data_nascimento">Data nascimento</label>
                            </td>
                            <td>
                                <input id="data_nascimento" name="data_nascimento" type="text"  value="<?= $respDados['data_nascimento'] ?>" >
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="data_batismo">Data Batismo</label>
                            </td>
                            <td>
                                <input id="data_batismo" name="data_batismo" type="text"  value="<?= $respDados['data_batismo'] ?>" >
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="eh_batizado_es">Batizado Espirito Santo</label>
                            </td>
                            <td>
                                <select name="eh_batizado_es">
                                    <option value="0" <?php print (($respDados['eh_batizado_es'] < 1) ? (" selected ") : ("")); ?> >nao</option>
                                    <option value="1" <?php print (($respDados['eh_batizado_es'] == 1) ? (" selected ") : ("")); ?> >sim</option>
                                </select>
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="data_batismo_es">Data Batismo Espirito Santo</label>
                            </td>
                            <td>
                                <input id="data_batismo_es" name="data_batismo_es" type="text"  value="<?= $respDados['data_batismo_es'] ?>" >
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="naturalidade">Naturalidade</label>
                            </td>
                            <td>
                                <input id="naturalidade" name="naturalidade" type="text"  value="<?= $respDados['naturalidade'] ?>" >
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="numero_registro">Numero Registro</label>
                            </td>
                            <td>
                                <input id="numero_registro" name="numero_registro" type="text"  value="<?= $respDados['numero_registro'] ?>" >
                            </td>
                        </tr>


                        <tr>
                            <td>
                                <label for="cargo_ministerial">Cargo Ministerial</label>
                            </td>
                            <td>
                                <?php echo listaCargo($respDados['cargo_ministerial']); ?>
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="igreja">Igreja</label>
                            </td>
                            <td>
                                <?php echo listaIgrejas($respDados['igreja']); ?>
                            </td>
                        </tr>


                        <tr>
                            <td>
                                    &nbsp;
                            </td>
                            <td>
                                    &nbsp;
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <input name="command" type="hidden" value="alteramembro" />
                                <input name="id" type="hidden" value="<?= $_GET['id'] ?>" />
                                <button type="submit" class="pure-button pure-button-primary">salvar</button>
                            </td>
                            <td>
                                <a href="index.php"><button type="button" class="pure-button pure-button-primary">Voltar</button></a>
                            </td>
                        </tr>


                    </table>
                </fieldset>
            </form>
        </body>
    </div>
</html>

