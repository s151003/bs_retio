#!/usr/bin/python
# -*- coding: utf-8 -*-
from ig import gaitame
from oanda import oanda
from xm import xm

gaitameSym, gaitameB, gaitameS = gaitame()
oandaSym, oandaB, oandaS = oanda()
xmSym, xmB, xmS = xm()

count = 0
print "外為どっとこむ"
for o in gaitameSym:

	print o
	print "B:",gaitameB[count]
	print "S:",gaitameS[count]
	count = count + 1

oandaS.append("haneisaren")

print "Oanda"
count = 0
for o in oandaSym:

	print o
	print "B:",oandaB[count]
	print "S:",oandaS[count]
	count = count + 1


print "XM"
count = 0
for o in xmSym:
	print o
	print "B:",xmB[count]
	print "S:",xmS[count]
	count = count + 1
