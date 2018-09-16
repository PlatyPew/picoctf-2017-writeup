# Little School Bus
Points: 75

## Category
Forensics

## Question
>Can you help me find the data in this [littleschoolbus.bmp](files/littleschoolbus.bmp)?

### Hint
>Look at least significant bit encoding!!

## Solution
Looking at the hint, we can use _zsteg_ to find the hidden info.

```
$ zsteg littleschoolbus.bmp
imagedata           .. text: "~vtsnljmkhhfgXWWNNNWTV"
b1,lsb,bY           .. text: "flag{remember_kids_protect_your_headers_b1bb}"
b3,r,lsb,xY         .. file: very old 16-bit-int big-endian archive
b4,rgb,msb,xY       .. file: MPEG ADTS, layer I, v2, 112 kbps, 24 kHz, JntStereo
```

We get the flag in _b1, lsb, bY_

### Flag
`flag{remember_kids_protect_your_headers_b1bb}`
