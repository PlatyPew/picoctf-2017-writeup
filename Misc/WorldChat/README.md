# WorldChat
Points: 30

## Category
Misc

## Question
>We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are so many other people talking that we can't really keep track of what is going on! Go see if you can find the messenger at shell2017.picoctf.com:44323. Remember to use Ctrl-C to cut the connection if it overwhelms you!

### Hint
>There are cool command line tools that can filter out lines with specific keywords in them. Check out 'grep'! You can use the '|' character to put all the output into another process or command (like the grep process)

## Solution
Connecting to the service by doing `nc shell2017.picoctf.com 44323`, we realise that `flagperson` gives us part of a flag

Now we just need to do `grep flagperson` and wait

```
$ nc shell2017.picoctf.com 44323 | grep flagperson
06:34:05 flagperson: this is part 1/8 of the flag - 7c20
06:34:15 flagperson: this is part 2/8 of the flag - 77dc
06:34:26 flagperson: this is part 3/8 of the flag - 26c1
06:34:27 flagperson: this is part 4/8 of the flag - 6dc8
06:34:29 flagperson: this is part 5/8 of the flag - 1acd
06:34:31 flagperson: this is part 6/8 of the flag - e49c
06:34:31 flagperson: this is part 7/8 of the flag - d563
06:34:35 flagperson: this is part 8/8 of the flag - 0146
```

Piece the flag together and we get the full flag

### Flag
`7c2077dc26c16dc81acde49cd5630146`
