# Leaf of the Tree
Points: 20

## Category
Misc

## Question
>We found this annoyingly named directory tree starting at /problems/e9c1c685270e96936e44ad5768f23ce3. It would be pretty lame to type out all of those directory names but maybe there is something in there worth finding? And maybe we dont need to type out all those names...? Follow the trunk, using cat and ls!

### Hint
>Tab completion is a wonderful, wonderful thing

## Solution
We can use the `find` command to find files that have the name `flag`

```
$ find . -type f -name flag -exec cat {} \; ; echo
b0e641edaceaa42e4d77e9f465516fdf
```

### Flag
`b0e641edaceaa42e4d77e9f465516fdf`
