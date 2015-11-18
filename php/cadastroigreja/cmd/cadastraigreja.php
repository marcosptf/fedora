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
                <div class="flash">Cadastra Igreja</div>
                <br/>
                <fieldset class="metanav">
                    <table class="add-entry">
                        <tr>
                            <td>
                                <label for="nameIgreja">Nome da Igreja:</label>
                            </td>
                            <td>
                                <input id="nome" name="nome" type="text" placeholder="">
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <label for="pais">Pais:</label>
                            </td>
                            <td>
                                <input id="pais" name="pais" type="text" placeholder="" />
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <label for="estado">Estado:</label>
                            </td>
                            <td>
                                <input id="estado" name="estado" type="text" placeholder="" />
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <label for="cidade">Cidade:</label>
                            </td>
                            <td>
                                <input id="cidade" name="cidade" type="text" placeholder="" />
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <label for="bairro">Bairro:</label>
                            </td>
                            <td>
                                <input id="bairro" name="bairro" type="text" placeholder="" />
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <label for="endereco">Endereco:</label>
                            </td>
                            <td>
                                <input id="endereco" name="endereco" type="text" placeholder="" />
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <label for="ministerio">CNPJ:</label>
                            </td>
                            <td>
                                <input id="ministerio" name="ministerio" type="text" placeholder="">
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <label for="setor">Setor:</label>
                            </td>
                            <td>
                                <input id="setor" name="setor" type="text" placeholder="">
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <label for="regional">Regional:</label>
                            </td>
                            <td>
                                <input id="regional" name="regional" type="text" placeholder="">
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
                                <input name="command" type="hidden" value="cadastraigreja" />
                                <button type="submit">Salvar</button>
                            </td>
                            <td>
                                <a href="index.php"><button type="button">Voltar</button></a>
                            </td>
                        </tr>
                    </table>
                </fieldset>
            </form>
        </body>
    </div>
</html>

