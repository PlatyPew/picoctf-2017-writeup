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
