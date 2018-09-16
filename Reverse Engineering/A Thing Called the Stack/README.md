# A Thing Called the Stack
Points: 60

## Category
Reverse Engineering

## Question
>A friend was stacking dinner plates, and handed you [this](files/assembly.s), saying something about a "stack". Can you find the difference between the value of esp at the end of the code, and the location of the saved return address? Assume a 32 bit system. Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df

### Hint
>Where is the return address saved on the stack?
>
>Which commands actually affect the stack?

## Solution
Taking the assembly code given, we can see that it is pushing values into a stack.

```asm
foo:
    pushl %ebp
    mov %esp, %ebp
    pushl %edi
    pushl %esi
    pushl %ebx
    sub $0x90, %esp
    movl $0x1, (%esp)
    movl $0x2, 0x4(%esp)
    movl $0x3, 0x8(%esp)
    movl $0x4, 0xc(%esp)
```

From the code, we can see that the stack is initialised to be _0x90_ bytes long. However, 4 values have been pushed into the stack. As such, we can calculate where the _esp_ is from the return address.

Since each value pushed into the stack is 4 bytes, we have to take that into account. We take _4 bytes_ multiplied by _4 values_. We then add that to the initialised stack size.

```python
>>> hex(4 * 4 + 0x90)
'0xa0'
```

### Flag
`0xa0`