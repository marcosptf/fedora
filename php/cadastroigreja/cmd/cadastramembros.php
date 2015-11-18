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
            <form action="../app/engine/command.php" method="post">
                <div class="flash">Cadastra Membros</div>
                <br>
                <fieldset class="metanav">

                    <table class="add-entry">
                        <tr>
                            <td>
                                <label for="nome">Nome</label>
                            </td>
                            <td>
                                <input id="nome" name="nome" type="text">
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="nome_pai">Nome do Pai</label>
                            </td>
                            <td>
                                <input id="nome_pai" name="nome_pai" type="text" />
                            </td>
                        </tr>


                        <tr>
                            <td>
                                <label for="nome_mae">Nome mae</label>
                            </td>
                            <td>
                                <input id="nome_mae" name="nome_mae" type="text" />
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="rg">RG</label>
                            </td>
                            <td>
                                <input id="rg" name="rg" type="text" />
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="cpf">CPF</label>
                            </td>
                            <td>
                                <input id="cpf" name="cpf" type="text"  />
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="idade">idade</label>
                            </td>
                            <td>
                                <input id="idade" name="idade" type="text"  />
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="data_nascimento">Data nascimento</label>
                            </td>
                            <td>
                                <input id="data_nascimento" name="data_nascimento" type="text" >
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="data_batismo">Data Batismo</label>
                            </td>
                            <td>
                                <input id="data_batismo" name="data_batismo" type="text" >
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="eh_batizado_es">Batizado Espirito Santo</label>
                            </td>
                            <td>
                                <select name="eh_batizado_es">
                                    <option value="0">nao</option>
                                    <option value="1">sim</option>
                                </select>
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="data_batismo_es">Data Batismo Espirito Santo</label>
                            </td>
                            <td>
                                <input id="data_batismo_es" name="data_batismo_es" type="text" >
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="naturalidade">Naturalidade</label>
                            </td>
                            <td>
                                <input id="naturalidade" name="naturalidade" type="text" >
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="numero_registro">Numero Registro</label>
                            </td>
                            <td>
                                <input id="numero_registro" name="numero_registro" type="text" >
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="cargo_ministerial">Cargo Ministerial</label>
                            </td>
                            <td>
                                <?php echo listaCargo(); ?>
                            </td>
                        </tr>



                        <tr>
                            <td>
                                <label for="igreja">Igreja</label>
                            </td>
                            <td>
                                <?php echo listaIgrejas(); ?>
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
                                <input name="command" type="hidden" value="cadastramembro" />
                                <button type="submit" >salvar</button>
                            </td>
                            <td>
                                <a href="index.php"><button type="button" >Voltar</button></a>
                            </td>
                        </tr>


                    </table>
                </fieldset>
            </form>
        </body>
    </div>
</html>

