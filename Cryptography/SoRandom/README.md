# SoRandom
Points: 75

## Category
Cryptography

## Question
>We found [sorandom.py](files/sorandom.py) running at shell2017.picoctf.com:37968. It seems to be outputting the flag but randomizing all the characters first. Is there anyway to get back the original flag?

### Hint
>How random can computers be?

## Solution
We are given the Python script _sorandom.py_, which contains what looks like to be a form of rotational cipher, fed with random values. How are we going to figure what the flag is without brute-forcing?

```python
import random,string

flag = "FLAG:"+open("flag", "r").read()[:-1]
encflag = ""
random.seed("random")
for c in flag:
  if c.islower():
    #rotate number around alphabet a random amount
    encflag += chr((ord(c)-ord('a')+random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
    encflag += chr((ord(c)-ord('A')+random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
    encflag += chr((ord(c)-ord('0')+random.randrange(0,10))%10 + ord('0'))
  else:
    encflag += c
print "Unguessably Randomized Flag: "+encflag
```

In the beginning of the script, it does `random.seed("random")`, which sets a seed for the randomiser. This means that Python will generate the same numbers for every runtime as long as the seed used is the string _"random"_

We can visit the remote service hosted on _shell2017.picoctf.com:37968_ to get the encrypted flag.

```bash
$ nc shell2017.picoctf.com 37968
Unguessably Randomized Flag: BNZQ:jn0y1313td7975784y0361tp3xou1g44
```

Now, we can write a script that will reverse the cipher.

First, we feed in the seed _"random"_, and the encrypted flag. We then use the same code, but do a `26 - num` to reverse the order. For example, if the character is rotated by _3_, we can do `26-3` to get _23_, which is the rotation required to get back the original letter.

```python
#!/usr/bin/env python2

import random

random.seed('random')
flag = 'BNZQ:jn0y1313td7975784y0361tp3xou1g44'

finalFlag = ''
for c in flag:
	if c.islower():
		finalFlag += chr((ord(c)-ord('a')+(26-random.randrange(0,26)))%26 + ord('a'))
	elif c.isupper():
		finalFlag += chr((ord(c)-ord('A')+(26-random.randrange(0,26)))%26 + ord('A'))
	elif c.isdigit():
		finalFlag += chr((ord(c)-ord('0')+(10-random.randrange(0,10)))%10 + ord('0'))
	else:
		finalFlag += c

print finalFlag
```

Working solution [solve.py](solution/solve.py)

### Flag
`ac8c0490fb0508767f1625cb8cea8c34`
