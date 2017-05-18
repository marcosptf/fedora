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
