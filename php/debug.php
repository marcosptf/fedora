<?php

function a(){
	print("a");
	function bb(){
		print("bb");
		function ccc(){
			print("ccc");
			function dddd(){
				print("dddd");
				function eeeee(){
					print("eeeee");
				}
				eeeee();
			}
			dddd();
		}
		ccc();	
	}
	bb();
	eeeee();
}
a();
#====>
#abbcccddddeeeeeeeeee


$b = "varb";

$a = function () use ($b) {
	return("php-debugger=>{$b}");
};

var_export($a());
#===>
#'php-debugger=>varb'
