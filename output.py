#!/usr/bin/python
# -*- coding: utf-8 -*-
from gaitame import gaitame
from oanda import oanda
from xm import xm

requestSym = "USD/JPY"

gaitameSym, gaitameB, gaitameS, gaitameFound = gaitame(requestSym)
oandaSym, oandaB, oandaS, oandaFound = oanda(requestSym)
xmSym, xmB, xmS, xmFound = xm(requestSym)


def disp_all():
	print "------- 外為どっとこむ -------"
	count = 0
	for o in gaitameSym:
		print o
		print "B:",gaitameB[count]
		print "S:",gaitameS[count]
		count = count + 1

	print "------- Oanda -------"
	count = 0
	oandaS.append("haneisaren")
	for o in oandaSym:
		print o
		print "B:",oandaB[count]
		print "S:",oandaS[count]
		count = count + 1

	print "------- XM -------"
	count = 0
	for o in xmSym:
		print o
		print "B:",xmB[count],"%"
		print "S:",xmS[count],"%"
		count = count + 1

def disp(requestSym):
	# 代入してからじゃないとエラー
	oanda = oandaFound - 1
	xm = xmFound - 1
	gaitame = gaitameFound - 1
	# なんで？？？？
	# local variable 'oandaFound' referenced before assignment

	print "------- 外為どっとこむ -------"
	print gaitameSym[gaitame]
	print "B:",gaitameB[gaitame]
	print "S:",gaitameS[gaitame]

	print "------- Oanda -------"
	print oandaSym[oanda]
	print "B:",oandaB[oanda]
	print "S:",oandaS[oanda]

	print "------- XM -------"
	print xmSym[xm]
	print "B:",xmB[xm]
	print "S:",xmS[xm]


if requestSym is "All":
	disp_all()
else:
	disp(requestSym)
