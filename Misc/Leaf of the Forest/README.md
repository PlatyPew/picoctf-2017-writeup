# Leaf of the Forest
Points: 30

## Category
Misc

## Question
>We found an even bigger directory tree hiding a flag starting at /problems/d9fbdb968961f708989999193aaca05d. It would be impossible to find the file named flag manually...

### Hint
>Is there a search function in Linux? Like if I wanted to 'find' something...

## Solution
Same thing as [Leaf of the Tree](Leaf%20of%20the%20Tree)

```
$ find . -type f -name flag -exec cat {} \; ; echo
e553af78ff1f7a6a428456ac53d837e5
```

### Flag
`e553af78ff1f7a6a428456ac53d837e5`
