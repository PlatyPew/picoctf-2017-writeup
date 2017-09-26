# computeRSA
Points: 50

## Category
Cryptography

## Question
>RSA encryption/decryption is based on a formula that anyone can find and use, as long as they know the values to plug in. Given the encrypted number 150815, d = 1941, and N = 435979, what is the decrypted number?

### Hint
>decrypted = (encrypted) ^ d mod N

## Solution
Just follow the hint...

```python
>>> 150815 ** 1941 % 435979
133337
```

### Flag
`133337`
