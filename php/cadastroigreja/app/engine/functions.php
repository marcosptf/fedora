<?php

function logme($message){
    $file = '/home/security-integrations/net-helpdesk-integration/log/' . date("D-M-Y") . '.txt';
    throw new Exception($message);
}

function logmeMySql($message){
    mysql_query("insert into logs (descricao) values ('{$message}');");
}

function listaIgrejas($param=0){
    $respHtml = "<select name='igreja'>";
    $sqlQuery = "select id,nome from igrejas;";
    $respQuery = mysql_query($sqlQuery);
    $respHtml.= "<option value=''>&nbsp;</option>";
    
    while($respFetch = mysql_fetch_array($respQuery)){
        $respHtml.= "<option value='{$respFetch['id']}' ".(($param==$respFetch['id']) ? ("selected") : (""))." >{$respFetch['nome']}</option>";
    }
    $respHtml.= "</select>";
    return $respHtml;
}

function listaCargo($param=0){
    $respHtml = "<select name='cargo_ministerial'>";
    $sqlQuery = "select id,descricao_cargo from param_cargo_ministerial;";
    $respQuery = mysql_query($sqlQuery);
    $respHtml.= "<option value=''>&nbsp;</option>";
    
    while($respFetch = mysql_fetch_array($respQuery)){
        $respHtml.= "<option value='{$respFetch['id']}' ".(($param==$respFetch['id']) ? ("selected") : (""))." >{$respFetch['descricao_cargo']}</option>";
    }
    $respHtml.= "</select>";
    return $respHtml;
}

function listaMembros(){
    $respHtml = "<select name='membros'>";
    $sqlQuery = "select id,nome from membros;";
    $respQuery = mysql_query($sqlQuery);
    $respHtml.= "<option value=''>&nbsp;</option>";
    
    while($respFetch = mysql_fetch_array($respQuery)){
        $respHtml.= "<option value='{$respFetch['id']}'>{$respFetch['nome']}</option>";
    }
    $respHtml.= "</select>";
    return $respHtml;
}


function buscaMembros($busca){
    $respHtml = "";
    $sqlQuery = "select id,nome from membros where nome like '%{$busca}%';";
    $respQuery = mysql_query($sqlQuery);
    
    while($respFetch = mysql_fetch_array($respQuery)){
        $respHtml.= "<a href='membros.php?id={$respFetch['id']}'>{$respFetch['nome']}</a><br/>";
    }
    return $respHtml;
}

function buscaIgreja($busca){
    $respHtml = "";
//    $sqlQuery = "select id,nome from igrejas where id='{$busca}';";
    $sqlQuery = "select id,nome from igrejas;";
    $respQuery = mysql_query($sqlQuery);
    
    while($respFetch = mysql_fetch_array($respQuery)){
        $respHtml.= "<a href='igreja.php?id={{$respFetch['id']}}'>{$respFetch['nome']}</a><br/>";
    }
    $respHtml.= "</select>";
    return $respHtml;
}

function buscaDadosIgreja($busca){
    $sqlQuery = "select id,nome,endereco,pais,estado,cidade,bairro,ministerio,setor,regional,id_membro_resp_igreja from igrejas where id='{$busca['igreja']}';";
    $respQuery = mysql_query($sqlQuery);
    return mysql_fetch_array($respQuery);
}

function buscaDadosMembros($busca){
    $sqlQuery = "select membros.id,membros.id_igreja,nome,nome_pai,nome_mae,rg,cpf,idade,data_nascimento,data_batismo,eh_batizado_es,data_batismo_es,naturalidade,cargo_ministerial,numero_registro,foto,param_igreja_x_membro.id_igreja as igreja from membros inner join param_igreja_x_membro on param_igreja_x_membro.id_membro=membros.id where membros.id='{$busca}';;";
    $respQuery = mysql_query($sqlQuery);
    return mysql_fetch_array($respQuery);
}


function cadastraIgreja($dados){
    $sqlInsert="
        insert into igrejas
        (nome,endereco,pais,estado,cidade,bairro,ministerio,setor,regional)
        values
        ('{$dados['nome']}','{$dados['endereco']}','{$dados['pais']}','{$dados['estado']}','{$dados['cidade']}','{$dados['bairro']}','{$dados['ministerio']}','{$dados['setor']}','{$dados['regional']}');";
    mysql_query($sqlInsert);
}

function logon($dados){
  $sqlQuery="
        select  usuario,senha
        from    usuarios
        where   usuario='{$dados['usuario']}'
        and     senha=  '{$dados['senha']}';";
    return mysql_num_rows(mysql_query($sqlQuery));
}

function cadastrandoMembro($dados){
    $sqlInsertMembros="
        insert into membros
        (nome,nome_pai,nome_mae,rg,cpf,idade,data_nascimento,data_batismo,eh_batizado_es,data_batismo_es,naturalidade,numero_registro,cargo_ministerial)
        values
        ('{$dados['nome']}','{$dados['nome_pai']}','{$dados['nome_mae']}','{$dados['rg']}','{$dados['cpf']}','{$dados['idade']}','{$dados['data_nascimento']}','{$dados['data_batismo']}','{$dados['eh_batizado_es']}','{$dados['data_batismo_es']}','{$dados['naturalidade']}','{$dados['numero_registro']}','{$dados['cargo_ministerial']}');";
    mysql_query($sqlInsertMembros);
    
    $sqlInsertIgrejaMembro="
        insert into param_igreja_x_membro
        (id_igreja,id_membro)
        values
        ('{$dados['igreja']}','".mysql_insert_id()."');";
    mysql_query($sqlInsertIgrejaMembro);
}

function alteraMembro($dados){
    $sqlInsertMembros="
        update      membros
        set         nome='{$dados['nome']}',
                    nome_pai='{$dados['nome_pai']}',
                    nome_mae='{$dados['nome_mae']}',
                    rg='{$dados['rg']}',
                    cpf='{$dados['cpf']}',
                    idade='{$dados['idade']}',
                    data_nascimento='{$dados['data_nascimento']}',
                    data_batismo='{$dados['data_batismo']}',
                    eh_batizado_es='{$dados['eh_batizado_es']}',
                    data_batismo_es='{$dados['data_batismo_es']}',
                    naturalidade='{$dados['naturalidade']}',
                    numero_registro='{$dados['numero_registro']}',
                    cargo_ministerial='{$dados['cargo_ministerial']}'
        where       id='{$dados['id']}';";
    mysql_query($sqlInsertMembros);
    $sqlInsertMembros="
        update      param_igreja_x_membro
        set         id_igreja='{$dados['igreja']}'
        where       id_membro='{$dados['id']}';";
    mysql_query($sqlInsertMembros);
}

function alteraIgreja($dados){
    $sqlInsertMembros="
        update      igrejas
        set         nome='{$dados['nome']}',
                    endereco='{$dados['endereco']}',
                    pais='{$dados['pais']}',
                    estado='{$dados['estado']}',
                    cidade='{$dados['cidade']}',
                    bairro='{$dados['bairro']}',
                    ministerio='{$dados['ministerio']}',
                    setor='{$dados['setor']}',
                    regional='{$dados['regional']}'
        where       id='{$dados['id']}';";
    mysql_query($sqlInsertMembros);
}