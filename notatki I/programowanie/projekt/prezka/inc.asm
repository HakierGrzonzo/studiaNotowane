    lda ($fb),y // load from (($fb)* + y)*
    cmp #$ff    // compare to 255
    beq label() // if acc == 255 go to label
    clc         // clear carry flag
    adc #$01    // acc = acc + 1 + carry
    sta ($fb),y // store to (($fb)* + y)
label():
