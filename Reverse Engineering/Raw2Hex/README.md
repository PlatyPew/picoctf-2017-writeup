# Raw2Hex
Points: 20

## Category
Reverse Engineering

## Question
>This program just prints a flag in raw form. All we need to do is convert the output to hex and we have it! CLI yourself to /problems/40b1e663252261e8203962486523629e and turn that Raw2Hex!

### Hint
>Google is always very helpful in these circumstances. In this case, you should be looking for an easy solution.

## Solution
Upon executing the binary, we are shown this:
```
$ ./raw2hex
The flag is:qux8&S┌▒├≤@░␊┌┌↑┬...
```

A bunch of gibberish shows up.

From the question text, the flag is that gibberish in hex

Converting it to hex
```
$ ./raw2hex | xxd -pu
54686520666c61672069733a71c28db77578a80e38aae0d626d853a5
```

Remove the first 24 characters because that is the text `The flag is:` in hex

### Flag
`71c28db77578a80e38aae0d626d853a5`
