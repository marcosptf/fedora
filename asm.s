#arquivo assembly para escrever comentario ate o fim da linha
#para compilar:
#as asm.s -o asm.o
#ld asm.o -o asm 
#./asm
#
.text
.section .data
    .equ SYS_WRITE, 4
    .equ LINUX_SYSCALL, 0x80

.global _start
_start:
    movl $TAMANH,%edx
    movl $1,%ebx
    movl $SYS_WRITE,%eax
    int  $LINUX_SYSCALL
    movl $0,%ebx
    movl $1,%eax
    int  $LINUX_SYSCALL
.data
msg:
    .ascii "ola mundo finalmente vivo"
    TAMANH = . - msg


