;hello word .asm nasm
;example code asm nasm compiler
;

	global _main
	extern _printf

	section .text

	
_main:
	push 	message
	call	_printf
	add     esp,4
	ret

message:
	db	'hello, word',10,0


