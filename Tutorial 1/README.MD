# Tutorial 1

## Category
Tutorial

## Question
>How can you figure out Robin Morris's middle name? Thankfully you have a [list](contractors.txt) you can check!

### Hint
>Please don't search by hand!

## Solution
Using `grep`, we can use a little regex to find Robin's middle name.

`cat contractors.txt | grep -E "^Robin .* Morris$"`

### Flag
`Almay`
