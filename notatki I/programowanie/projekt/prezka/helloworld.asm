BasicUpstart2(start)      // tell BASIC to start execution at `start'
*=$4000 "Program"         // at memory $4000 place
start:         
    ldy #$00              // store 0 to register Y
print_loop:
    lda string, Y         // load to accumulator (string + Y)*
    cmp #$00              // compare it to 0
    beq loop              // if equal goto loop
    jsr $ffd2             // jump to kernal function for printing
    iny                   // Y++
    jmp print_loop        // goto print_loop
loop:
    jmp loop              // goto loop
string:
    .text "HELLO, WORLD!" // place text in memory
    .byte 0               // cstring ends with a zero byte
