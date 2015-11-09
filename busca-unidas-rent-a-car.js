/**
 * @author:Marcos Paulo
 * @since:15/03/2012
 * @desc:regra js de toda interação do usuario com os filtros de busca
 * comum e avançada;
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

idMontadora = '';
modeloCarro = '';
anoModelo	= '';
lojaSel 	= '';
preco		= '';
preco2		= '';
inAjax		= 0;

var comboPreco,buscaCmd;
comboPreco ="<option value=''>Selecione Preço...</option>"+
            "<option value='1'>R$ 10.000,00 a R$ 15.000,00</option>"+
            "<option value='2'>R$ 15.000,00 a R$ 20.000,00</option>"+
            "<option value='3'>R$ 20.000,00 a R$ 25.000,00</option>"+
            "<option value='4'>R$ 25.000,00 a R$ 30.000,00</option>"+
            "<option value='5'>R$ 30.000,00 a R$ 35.000,00</option>"+
            "<option value='6'>R$ 35.000,00 a R$ 40.000,00</option>"+
            "<option value='7'>R$ 40.000,00 a R$ 45.000,00</option>"+
            "<option value='8'>R$ 45.000,00 a R$ 50.000,00</option>"+
            "<option value='9'>R$ 50.000,00 a R$ 55.000,00</option>"+
            "<option value='10'>R$ 50.000,00 a R$ 55.000,00</option>"+
            "<option value='11'>R$ 55.000,00 a R$ 60.000,00</option>"+
            "<option value='12'>R$ 60.000,00 a R$ 65.000,00</option>"+
            "<option value='13'>R$ 65.000,00 a R$ 70.000,00</option>"+
			"<option value='15'>Acima de R$ 70.000,00</option>";

buscaCmd="http://site.unidas.com.br/wp-content/themes/unidas/busca.cmd.php";

function uncheckMarcas(){
	//removeClass()
	$("#fi").removeClass('marca_ativa');
	$("#gm").removeClass('marca_ativa');
	$("#for").removeClass('marca_ativa');	
	$("#ren").removeClass('marca_ativa');
	$("#toy").removeClass('marca_ativa');
	$("#vw").removeClass('marca_ativa');
	$("#nis").removeClass('marca_ativa');
	$("#hon").removeClass('marca_ativa');
	$("#mit").removeClass('marca_ativa');
	$("#hyu").removeClass('marca_ativa');	
	$("#peu").removeClass('marca_ativa');	
}

function loadAjax(){
  $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
}

function selectModelo()
{
	if (modeloCarro != '')
	{
		$('#sltModelo').val(modeloCarro).change();
		modeloCarro = '';
	}	
}

function selectPreco()
{
	if ((preco != '') && (lojaSel != '') && (anoModelo == '') && (modeloCarro == ''))
	{
		$('#sltPreco1').val(preco).change();
		preco = '';
	}
	
	if ((preco2 != '') && (lojaSel != '') && (anoModelo == '') && (modeloCarro == ''))
	{
		$('#sltPreco2').val(preco2).change();
		preco2 = ''
	}	
}

function selectAnoModelo()
{
	if ((anoModelo != '') && (modeloCarro == ''))
	{
		$("#anoModelo").val(anoModelo).change();
	}
}


function selectLoja()
{
	if ((lojaSel != '') && (anoModelo == '') && (modeloCarro == ''))
	{
		$("#sltLojas").val(lojaSel).change();
		
		lojaSel = '';
	}
}

function disableLoading()
{
	inAjax--;
	
	if (!inAjax)
		document.getElementById("loadAjax").style.display="none";
}

$(document).ready(function(){

	$("#sltPreco1, #sltPreco2").numeric({ decimal: false, negative: false }, function() { alert("Informe somente números."); this.value = ""; this.focus(); });
	
/*******************************************************************************
* Busca para a Maravilhosa Marca de Carros Fiat  :-)
********************************************************************************/


        $('#fi').click(function() {
			$("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			uncheckMarcas();			
            $(this).addClass('marca_ativa');
            $("#MarcaSelect").val("fiat");
			$(".marca p").html("Fiat");
            $("#sltModelo").html("<option value=''>Selecione Modelo...</option>");
			$("#anoModelo").html("<option value=''>Ano Modelo...</option>");
            $("#sltLojas").html("<option value=''>Selecione Lojas...</option>");
            $("#sltPreco1").val("");
			$("#sltPreco2").val("");

			inAjax++;
            $.post(buscaCmd,{qtdCarrosEstoque:1,marca:"fiat" },
                function(dataQtdeCarros){
                        document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md=&pc=&lj=";
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+dataQtdeCarros+" carro(s) para você");

                        if(dataQtdeCarros > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }

            }).complete(function()
			{
				disableLoading();
			});

			inAjax++;
            $.post(buscaCmd,{marca:"fiat" },
                function(dataModelo){
                $("#sltModelo").html(dataModelo);
				selectModelo();
            }).complete(function()
			{
				disableLoading();
			});
			
			if (modeloCarro == '')
			{
				inAjax++;
				$.post(buscaCmd,{marca:"fiat", anoModelo:1},
					function(dataModelo){					
						$("#anoModelo").html(dataModelo);
						selectAnoModelo();
				}).complete(function()
				{
					disableLoading();
				});

				inAjax++;
				$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val()},
					function(dataLoja){
					$("#sltLojas").html(dataLoja);
					selectLoja();
				}).complete(function()
				{
					disableLoading();
				});
				
				selectPreco();
			}
						
			document.getElementById("respQtdeCarros").style.display="block";

         });

        $('#fi').hover( function() { $("ul.marcas").removeClass().toggleClass("marcas fiat"); }, function() { $("ul.marcas").removeClass("fiat"); } );



/*******************************************************************************
* Busca para a FORD
********************************************************************************/


        $('#for').click(function() {
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			uncheckMarcas();
//            $("button.marcas").removeClass().toggleClass("marcas ford");
            $("#MarcaSelect").val("ford");
			$(".marca p").html("Ford");
            $(this).addClass('marca_ativa');
            $("#sltModelo").html("<option value=''>Selecione Modelo...</option>");
			$("#anoModelo").html("<option value=''>Ano Modelo...</option>");
            $("#sltLojas").html("<option value=''>Selecione Lojas...</option>");
            $("#sltPreco1").val("");
			$("#sltPreco2").val("");

			inAjax++;
            $.post(buscaCmd,{qtdCarrosEstoque:1,marca:"ford" },
                function(data){
                        document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md=&pc=&lj=";
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }

            }).complete(function()
			{
				disableLoading();
			});

			inAjax++;
            $.post(buscaCmd,{marca:"ford" },
                function(data){
					$("#sltModelo").html(data);
					selectModelo();
            }).complete(function()
			{
				disableLoading();
			});
			
			if (modeloCarro == '')
			{
				inAjax++;
				$.post(buscaCmd,{marca:"ford", anoModelo:1},
					function(dataModelo){					
						$("#anoModelo").html(dataModelo);
						selectAnoModelo();
				}).complete(function()
				{
					disableLoading();
				});

				inAjax++;
				$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val()},
					function(data){
					$("#sltLojas").html(data);
					selectLoja();
				}).complete(function()
				{
					disableLoading();
				});
				
				selectPreco();
			}
			
			document.getElementById("respQtdeCarros").style.display="block";
        });
        $('#for').hover( function() { $("ul.marcas").removeClass().toggleClass("marcas ford"); }, function() { $("ul.marcas").removeClass("ford"); } );


/*******************************************************************************
* Busca para a GM
********************************************************************************/
        $('#gm').click(function() {
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			uncheckMarcas();
//            $("button.marcas").removeClass().toggleClass("marcas chevrolet");
            $("#MarcaSelect").val("chevrolet");
			$(".marca p").html("Chevrolet");
            $(this).addClass('marca_ativa');
            $("#sltModelo").html("<option value=''>Selecione Modelo...</option>");
			$("#anoModelo").html("<option value=''>Ano Modelo...</option>");
            $("#sltLojas").html("<option value=''>Selecione Lojas...</option>");
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
            $("#sltPreco1").val("");
			$("#sltPreco2").val("");
			
			inAjax++;
            $.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val() },
                function(data){
                        document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md=&pc=&lj=";
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }

            }).complete(function()
			{
				disableLoading();
			});

			inAjax++;
            $.post(buscaCmd,{marca:"chevrolet" },
                function(data){
					$("#sltModelo").html(data);
					selectModelo();
            }).complete(function()
			{
				disableLoading();
			});
			
			if (modeloCarro == '')
			{
				inAjax++;
				$.post(buscaCmd,{marca:"chevrolet", anoModelo:1},
					function(dataModelo){					
						$("#anoModelo").html(dataModelo);
						selectAnoModelo();
				}).complete(function()
				{
					disableLoading();
				});

				inAjax++;
				$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val()},
					function(data){
					$("#sltLojas").html(data);
					selectLoja();
				}).complete(function()
				{
					disableLoading();
				});
			   
				selectPreco();
			}
			
			document.getElementById("respQtdeCarros").style.display="block";
        });

        $('#gm').hover( function() { $("ul.marcas").removeClass().toggleClass("marcas chevrolet"); }, function() { $("ul.marcas").removeClass("chevrolet"); } );


/*******************************************************************************
* Busca para a Renault
********************************************************************************/

        $('#ren').click(function() {
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			uncheckMarcas();
//            $("button.marcas").removeClass().toggleClass("marcas renault");
            $("#MarcaSelect").val("renault");
			$(".marca p").html("Renault");
            $(this).addClass('marca_ativa');
            $("#sltModelo").html("<option value=''>Selecione Modelo...</option>");
			$("#anoModelo").html("<option value=''>Ano Modelo...</option>");
            $("#sltLojas").html("<option value=''>Selecione Lojas...</option>");
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
            $("#sltPreco1").val("");
			$("#sltPreco2").val("");

			inAjax++;
            $.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val() },
                function(data){
                        document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md=&pc=&lj=";
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }

            }).complete(function()
			{
				disableLoading();
			});

			inAjax++;
            $.post(buscaCmd,{marca:"renault" },
                function(data){
					$("#sltModelo").html(data);
					selectModelo();
            }).complete(function()
			{
				disableLoading();
			});
			
			if (modeloCarro == '')
			{
				inAjax++;
				$.post(buscaCmd,{marca:"renault", anoModelo:1},
					function(dataModelo){					
						$("#anoModelo").html(dataModelo);
						selectAnoModelo();
				}).complete(function()
				{
					disableLoading();
				});

				inAjax++;
				$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val()},
					function(data){
					$("#sltLojas").html(data);
					selectLoja();
				}).complete(function()
				{
					disableLoading();
				});
				
				selectPreco();
			}
			
			document.getElementById("respQtdeCarros").style.display="block";
        });

        $('#ren').hover( function() { $("ul.marcas").removeClass().toggleClass("marcas renault"); }, function() { $("ul.marcas").removeClass("renault"); } );

/*******************************************************************************
* Busca para a Toyota
********************************************************************************/

        $('#toy').click(function() {
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			uncheckMarcas();
//            $("button.marcas").removeClass().toggleClass("marcas toyota");
            $("#MarcaSelect").val("toyota");
			$(".marca p").html("Toyota");
            $(this).addClass('marca_ativa');
            $("#sltModelo").html("<option value=''>Selecione Modelo...</option>");
			$("#anoModelo").html("<option value=''>Ano Modelo...</option>");
            $("#sltLojas").html("<option value=''>Selecione Lojas...</option>");
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
            $("#sltPreco1").val("");
			$("#sltPreco2").val("");

			inAjax++;
            $.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val() },
                function(data){
                        document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md=&pc=&lj=";
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }

            }).complete(function()
			{
				disableLoading();
			});

			inAjax++;
            $.post(buscaCmd,{marca:"toyota" },
                function(data){
					$("#sltModelo").html(data);
					selectModelo();
            }).complete(function()
			{
				disableLoading();
			});
			
			if (modeloCarro == '')
			{
				inAjax++;
				$.post(buscaCmd,{marca:"toyota", anoModelo:1},
					function(dataModelo){					
						$("#anoModelo").html(dataModelo);
						selectAnoModelo();
				}).complete(function()
				{
					disableLoading();
				});

				inAjax++;
				$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val()},
					function(data){
					$("#sltLojas").html(data);
					selectLoja();
				}).complete(function()
				{
					disableLoading();
				});
				
				selectPreco();
			}
						
			document.getElementById("respQtdeCarros").style.display="block";
        });
        $('#toy').hover( function() { $("ul.marcas").removeClass().toggleClass("marcas toyota"); }, function() { $("ul.marcas").removeClass("toyota"); } );

/*******************************************************************************
* Busca para a VW
********************************************************************************/

        $('#vw').click(function() {
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			uncheckMarcas();			
//            $("button.marcas").removeClass().toggleClass("marcas volkswagen");
            $("#MarcaSelect").val("volkswagen");
			$(".marca p").html("Volkswagen");
            $(this).addClass('marca_ativa');
            $("#sltModelo").html("<option value=''>Selecione Modelo...</option>");
			$("#anoModelo").html("<option value=''>Ano Modelo...</option>");
            $("#sltLojas").html("<option value=''>Selecione Lojas...</option>");
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
            $("#sltPreco1").val("");
			$("#sltPreco2").val("");

			inAjax++;
            $.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val() },
                function(data){
                        document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md=&pc=&lj=";
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }

            }).complete(function()
			{
				disableLoading();
			});

			inAjax++;
            $.post(buscaCmd,{marca:"volkswagen" },
                function(data){
					$("#sltModelo").html(data);
					selectModelo();
            }).complete(function()
			{
				disableLoading();
			});
			
			if (modeloCarro == '')
			{
				inAjax++;
				$.post(buscaCmd,{marca:"volkswagen", anoModelo:1},
					function(dataModelo){					
						$("#anoModelo").html(dataModelo);
						selectAnoModelo();
				}).complete(function()
				{
					disableLoading();
				});

				inAjax++;
				$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val()},
					function(data){
					$("#sltLojas").html(data);
					selectLoja();
				}).complete(function()
				{
					disableLoading();
				});
				
				selectPreco();
			}
						
			document.getElementById("respQtdeCarros").style.display="block";
        });
        $('#vw').hover( function() { $("ul.marcas").removeClass().toggleClass("marcas volkswagen"); }, function() { $("ul.marcas").removeClass("volkswagen"); } );

/*******************************************************************************
* Busca para a Peugeot
********************************************************************************/


        $('#peu').click(function() {
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			uncheckMarcas();
//            $("button.marcas").removeClass().toggleClass("marcas peugeot");
            $("#MarcaSelect").val("peugeot");
			$(".marca p").html("Peugeot");
            $(this).addClass('marca_ativa');
            $("#sltModelo").html("<option value=''>Selecione Modelo...</option>");
			$("#anoModelo").html("<option value=''>Ano Modelo...</option>");
            $("#sltLojas").html("<option value=''>Selecione Lojas...</option>");
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
            $("#sltPreco1").val("");
			$("#sltPreco2").val("");

			inAjax++;
            $.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val() },
                function(data){
                        document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md=&pc=&lj=";
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }

            }).complete(function()
			{
				disableLoading();
			});

			inAjax++;
			$.post(buscaCmd,{marca:"peugeot" },
				function(data){
					$("#sltModelo").html(data);
					selectModelo();
				}).complete(function()
				{
					disableLoading();
				});
				
			if (modeloCarro == '')
			{
				inAjax++;
				$.post(buscaCmd,{marca:"peugeot", anoModelo:1},
					function(dataModelo){					
						$("#anoModelo").html(dataModelo);
						selectAnoModelo();
				}).complete(function()
				{
					disableLoading();
				});

				inAjax++;
				$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val()},
					function(data){
					$("#sltLojas").html(data);
					selectLoja();
				}).complete(function()
				{
					disableLoading();
				});
				
				selectPreco();
			}
			
			document.getElementById("respQtdeCarros").style.display="block";
        });
        $('#peu').hover( function() { $("ul.marcas").removeClass().toggleClass("marcas peugeot"); }, function() { $("ul.marcas").removeClass("peugeot"); } );

/*******************************************************************************
* Busca para a Honda
********************************************************************************/

        $('#hon').click(function() {
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			uncheckMarcas();			
//            $("button.marcas").removeClass().toggleClass("marcas honda");
            $("#MarcaSelect").val("honda");
			$(".marca p").html("Honda");
            $(this).addClass('marca_ativa');
            $("#sltModelo").html("<option value=''>Selecione Modelo...</option>");
			$("#anoModelo").html("<option value=''>Ano Modelo...</option>");
            $("#sltLojas").html("<option value=''>Selecione Lojas...</option>");
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
            $("#sltPreco1").val("");
			$("#sltPreco2").val("");

			inAjax++;
            $.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val() },
                function(data){
                        document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md=&pc=&lj=";
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }

            }).complete(function()
			{
				disableLoading();
			});

			inAjax++;
            $.post(buscaCmd,{marca:"honda" },
                function(data){
					$("#sltModelo").html(data);
					selectModelo();
            }).complete(function()
			{
				disableLoading();
			});
			
			if (modeloCarro == '')
			{
				inAjax++;
				$.post(buscaCmd,{marca:"honda", anoModelo:1},
					function(dataModelo){					
						$("#anoModelo").html(dataModelo);
						selectAnoModelo();
				}).complete(function()
				{
					disableLoading();
				});

				inAjax++;
				$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val()},
					function(data){
					$("#sltLojas").html(data);
					selectLoja();
				}).complete(function()
				{
					disableLoading();
				});
				
				selectPreco();
			}
						
			document.getElementById("respQtdeCarros").style.display="block";
        });
        $('#hon').hover( function() { $("ul.marcas").removeClass().toggleClass("marcas honda"); }, function() { $("ul.marcas").removeClass("honda"); } );

/*******************************************************************************
* Busca para a Mitsubishi
********************************************************************************/

        $('#mit').click(function() {
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			uncheckMarcas();
//            $("button.marcas").removeClass().toggleClass("marcas mitsubishi");
            $("#MarcaSelect").val("mitsubishi");
			$(".marca p").html("Mitsubishi");
            $(this).addClass('marca_ativa');
            $("#sltModelo").html("<option value=''>Selecione Modelo...</option>");
			$("#anoModelo").html("<option value=''>Ano Modelo...</option>");
            $("#sltLojas").html("<option value=''>Selecione Lojas...</option>");
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
            $("#sltPreco1").val("");
			$("#sltPreco2").val("");

			inAjax++;
            $.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val() },
                function(data){
                        document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md=&pc=&lj=";
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }

            }).complete(function()
			{
				disableLoading();
			});

            inAjax++;
			$.post(buscaCmd,{marca:"mitsubishi" },
                function(data){
					$("#sltModelo").html(data);
					selectModelo();
            }).complete(function()
			{
				disableLoading();
			});
			
			if (modeloCarro != '')
			{
				inAjax++;
				$.post(buscaCmd,{marca:"mitsubishi", anoModelo:1},
					function(dataModelo){					
						$("#anoModelo").html(dataModelo);
						selectAnoModelo();
				}).complete(function()
				{
					disableLoading();
				});

				inAjax++;
				$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val()},
					function(data){
					$("#sltLojas").html(data);
					selectLoja();
				}).complete(function()
				{
					disableLoading();
				});
				
				selectPreco();
			}
						
			document.getElementById("respQtdeCarros").style.display="block";
        });
        $('#mit').hover( function() { $("ul.marcas").removeClass().toggleClass("marcas mitsubishi"); }, function() { $("ul.marcas").removeClass("mitsubishi"); } );

/*******************************************************************************
* Busca para a Nissan
********************************************************************************/

        $('#nis').click(function() {
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			uncheckMarcas();			
//            $("button.marcas").removeClass().toggleClass("marcas nissan");
            $("#MarcaSelect").val("nissan");
			$(".marca p").html("Nissan");
            $(this).addClass('marca_ativa');
            $("#sltModelo").html("<option value=''>Selecione Modelo...</option>");
			$("#anoModelo").html("<option value=''>Ano Modelo...</option>");
            $("#sltLojas").html("<option value=''>Selecione Lojas...</option>");
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
            $("#sltPreco1").val("");
			$("#sltPreco2").val("");

			inAjax++;
            $.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val() },
                function(data){
                        document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md=&pc=&lj=";
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }

            }).complete(function()
			{
				disableLoading();
			});

            inAjax++;
			$.post(buscaCmd,{marca:"nissan" },
                function(data){
					$("#sltModelo").html(data);
					selectModelo();
            }).complete(function()
			{
				disableLoading();
			});
			
			if (modeloCarro == '')
			{			
				inAjax++;
				$.post(buscaCmd,{marca:"nissan", anoModelo:1},
					function(dataModelo){					
						$("#anoModelo").html(dataModelo);
						selectAnoModelo();
				}).complete(function()
				{
					disableLoading();
				});			

				inAjax++;
				$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val()},
					function(data){
					$("#sltLojas").html(data);
					selectLoja();
				}).complete(function()
				{
					disableLoading();
				});
				
				selectPreco();
			}
						
			document.getElementById("respQtdeCarros").style.display="block";
        });
        $('#nis').hover( function() { $("ul.marcas").removeClass().toggleClass("marcas nissan"); }, function() { $("ul.marcas").removeClass("nissan"); } );

/*******************************************************************************
* Busca para a Hyundai
********************************************************************************/

        $('#hyu').click(function() {
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			uncheckMarcas();			
//            $("button.marcas").removeClass().toggleClass("marcas hyundai");
            $("#MarcaSelect").val("hyundai");
			$(".marca p").html("Hyundai");
            $(this).addClass('marca_ativa');
            $("#sltModelo").html("<option value=''>Selecione Modelo...</option>");
			$("#anoModelo").html("<option value=''>Ano Modelo...</option>");
            $("#sltLojas").html("<option value=''>Selecione Lojas...</option>");
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
            $("#sltPreco1").val("");
			$("#sltPreco2").val("");

            inAjax++;
			$.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val() },
                function(data){
                        document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md=&pc=&lj=";
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }

            }).complete(function()
			{
				disableLoading();
			});

            inAjax++;
			$.post(buscaCmd,{marca:"hyundai" },
                function(data){
					$("#sltModelo").html(data);
					selectModelo();
            }).complete(function()
			{
				disableLoading();
			});
			
			if (modeloCarro == '')
			{			
				inAjax++;
				$.post(buscaCmd,{marca:"hyundai", anoModelo:1},
					function(dataModelo){					
						$("#anoModelo").html(dataModelo);
						selectAnoModelo();
				}).complete(function()
				{
					disableLoading();
				});

				inAjax++;
				$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val()},
					function(data){
					$("#sltLojas").html(data);
					selectLoja();
				}).complete(function()
				{
					disableLoading();
				});
				
				selectPreco();
			}
						
			document.getElementById("respQtdeCarros").style.display="block";
        });
        $('#hyu').hover( function() { $("ul.marcas").removeClass().toggleClass("marcas hyundai"); }, function() { $("ul.marcas").removeClass("hyundai"); } );


/*******************************************************************************
* Combo de Modelo
********************************************************************************/

        $('#sltModelo').change(function(){
			$("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";		
			nomeCarro = $(this).val();
			nomeCarro = nomeCarro.toLowerCase();
			nomeCarro = unescape(nomeCarro);
			$("#sltPreco1").val("");
			$("#sltPreco2").val("");
			$("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});			
            document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md="+nomeCarro+"&pc=&lj="+"&pc="+$('#sltPreco1').val()+"&pc2="+$('#sltPreco2').val();			

            inAjax++;
			$.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val(),modelo:nomeCarro },
                function(data){
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }
            }).complete(function()
			{
				disableLoading();
			});
			
			inAjax++;
			$.post(buscaCmd,{marca:$("#MarcaSelect").val(), modelo:nomeCarro, anoModelo:1},
                function(dataModelo){					
                    $("#anoModelo").html(dataModelo);
					selectAnoModelo();
            }).complete(function()
			{
				disableLoading();
			});

            inAjax++;
			$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val(),modelo:nomeCarro},
                function(data){				
                $("#sltLojas").html(data);
				selectLoja();
            }).complete(function()
			{
				disableLoading();
			});
			
			selectPreco();
						
			document.getElementById("respQtdeCarros").style.display="block";
        });
		
/*******************************************************************************
* Combo de Ano Modelo
********************************************************************************/
        $('#anoModelo').change(function(){
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";
			$("#sltPreco1").val("");
			$("#sltPreco2").val("");
            document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md="+$("#sltModelo").val()+"&pc="+$("#sltPreco1").val()+"&am="+$('#anoModelo').val()+"&pc="+$('#sltPreco1').val()+"&pc2="+$('#sltPreco2').val();
            
			inAjax++;
			$.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val(),modelo:$("#sltModelo").val(), anoModelo: $('#anoModelo').val(), preco:$("#sltPreco1").val(), preco2: $("#sltPreco2").val()},
                function(data)
				{
                    $(".info-load").css('display','block');
                    $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");
//                    $("#sltPreco2").html();

                    if(data > 0){
                        $('.content-visualizar').show("slow");
                        $('#btnBuscar').show("slow");
                    }else{
                        $('.content-visualizar').hide("slow");
                        $('#btnBuscar').hide("slow");
                    }
				}).complete(function()
				{
					disableLoading();
				});
				
            inAjax++;
			$.post(buscaCmd,{lojasPorMarca:1,marca:$("#MarcaSelect").val(),modelo:nomeCarro, anoModelo: $('#anoModelo').val()},
                function(data){
                $("#sltLojas").html(data);
				anoModelo = '';
				selectLoja();
            }).complete(function()
			{
				disableLoading();
			});				
			
			selectPreco();
						
			document.getElementById("respQtdeCarros").style.display="block";			
        });		

/*******************************************************************************
* Combo de preço
********************************************************************************/

        $('#sltPreco1, #sltPreco2').change(function(){
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";
            document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md="+$("#sltModelo").val()+"&am="+$("#anoModelo").val()+"&pc="+$('#sltPreco1').val()+"&pc2="+$('#sltPreco2').val()+"&lj="+$('#sltLojas').val();
            
			inAjax++;
			$.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val(),modelo:$("#sltModelo").val(), anoModelo: $("#anoModelo").val(), preco: $('#sltPreco1').val(), preco2: $('#sltPreco2').val(), lojas:$('#sltLojas').val()},
                function(data){
                        $(".info-load").css('display','block');
                        $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");

                        if(data > 0){
                            $('.content-visualizar').show("slow");
                            $('#btnBuscar').show("slow");
                        }else{
                            $('.content-visualizar').hide("slow");
                            $('#btnBuscar').hide("slow");
                        }
            }).complete(function()
			{
				disableLoading();
			});
					
			document.getElementById("respQtdeCarros").style.display="block";				
        });

/*******************************************************************************
* Combo de Lojas
********************************************************************************/
        $('#sltLojas').change(function(){
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";
			$("#sltPreco1").val("");
			$("#sltPreco2").val("");
            document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md="+$("#sltModelo").val()+"&pc="+$("#sltPreco1").val()+"&am="+$('#anoModelo').val()+"&lj="+this.value;
            
			inAjax++;
			$.post(buscaCmd,{qtdCarrosEstoque:1,marca:$("#MarcaSelect").val(),modelo:$("#sltModelo").val(), anoModelo: $('#anoModelo').val(), preco:$("#sltPreco1").val(), preco2: $("#sltPreco2").val(), lojas:this.value },
                function(data){
                    $(".info-load").css('display','block');
                    $("#respQtdeCarros").html("Estoque: Temos "+data+" carro(s) para você");
//                    $("#sltPreco2").html();

                    if(data > 0){
                        $('.content-visualizar').show("slow");
                        $('#btnBuscar').show("slow");
                    }else{
                        $('.content-visualizar').hide("slow");
                        $('#btnBuscar').hide("slow");
                    }
            }).complete(function()
			{
				disableLoading();
			});
			
			selectPreco();
						
			document.getElementById("respQtdeCarros").style.display="block";			
        });

/*******************************************************************************
* Combo de KM
********************************************************************************/
        $('#sltkm').change(function(){
            $("#loadAjax").css({'display' : 'inline-block', '*display' : 'inline', 'zoom' : '1'});
			document.getElementById("respQtdeCarros").style.display="none";
            document.getElementById("btnBuscar").href=path+"?mc="+$("#MarcaSelect").val()+"&md="+$("#sltModelo").val()+"&pc="+$("#sltPreco1").val()+"&lj="+$("#sltLojas").val()+"&km="+this.value;
            
			inAjax++;
			$.post(buscaCmd,{combokm:1,marca:$("#MarcaSelect").val(),modelo:$("#sltModelo").val(),preco:$("#sltPreco1").val(),lojas:$("#sltLojas").val(),km:this.value },
                function(respKM){
                    $(".info-load").css('display','block');
                    $("#respQtdeCarros").html("Estoque: Temos "+respKM+" carro(s) para você");

                    if(respKM > 0){
                        $('.content-visualizar').show("slow");
                        $('#btnBuscar').show("slow");
                    }else{
                        $('.content-visualizar').hide("slow");
                        $('#btnBuscar').hide("slow");
                    }
            }).complete(function()
			{
				disableLoading();
			});
			
			document.getElementById("respQtdeCarros").style.display="block";			
        });


/*******************************************************************************
* radio para selecionar entre busca comum e busca avançada.
********************************************************************************/
        $("#rdAvancada").click(function(){
           $("#divKM").show("slow");
        });

        $("#rdComum").click(function(){
            $("#divKM").hide("slow");
        });

/*******************************************************************************
*coisas do Jhomar Nando ?!?!??!?
********************************************************************************/

        $('ul.tipo-busca li a:first').click(function() {
                $("ul.tipo-busca li a:last").removeClass();
                $("ul.tipo-busca li a:first").toggleClass("current");
        });

        $('ul.tipo-busca li a:last').click(function() {
                $("ul.tipo-busca li a:first").removeClass();
                $("ul.tipo-busca li a:last").toggleClass("current");
        });
		
	if (idMontadora != '')
	{
		$('#' + idMontadora).click();
		
		idMontadora = '';
	}
});	

