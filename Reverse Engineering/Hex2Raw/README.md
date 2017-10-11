# Hex2Raw
Points: 20

## Category
Reverse Engineering

## Question
>This program requires some unprintable characters as input... But how do you print unprintable characters? CLI yourself to /problems/3ced8dfe6c77c63010c94a84656fa6ea and turn that Hex2Raw!

### Hint
>Google for easy techniques of getting raw output to command line. In this case, you should be looking for an easy solution.

## Solution
Upon executing the binary, we are shown this:
```
$ ./hex2raw
Give me this in raw form (0x41 -> 'A'):
1a558acddabd64bbccdd94903eafdf18

You gave me:
```

From this line `(0x41 -> 'A')`, we find out that the program is converting the ascii values to hex

Therefore, all we have to do is use a little bit of inline Python scripting to get the flag
```
$ python -c "print '\x1a\x55\x8a\xcd\xda\xbd\x64\xbb\xcc\xdd\x94\x90\x3e\xaf\xdf\x18'"|./hex2raw
Give me this in raw form (0x41 -> 'A'):
1a558acddabd64bbccdd94903eafdf18

You gave me:
1a558acddabd64bbccdd94903eafdf18
Yay! That's what I wanted! Here be the flag:
ceb80093717fd7e9aae149dacc7ac9b3
```

### Flag
`ceb80093717fd7e9aae149dacc7ac9b3`
