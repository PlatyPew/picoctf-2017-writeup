# Internet Kitties
Points: 10

## Category
Misc

## Question
>I was told there was something at IP shell2017.picoctf.com with port 2720. How do I get there? Do I need a ship for the port?

### Hint
>Look at using the netcat (nc) command!
>
>To figure out how to use it, you can run "man nc" or "nc -h" on the shell, or search for it on the interwebz

## Solution
Connect to the service via netcat

```
$ nc shell2017.picoctf.com 2720
Yay! You made it!
Take a flag!
0385d4bad438ffd596c049d5796e83a2
```

### Flag
`0385d4bad438ffd596c049d5796e83a2`
