#!/usr/bin/python
# -*- coding: utf-8 -*-
from gaitame import gaitame
from oanda import oanda
from xm import xm
from moneyparty import money
from minfx import minfx

requestSym = "USD/JPY"

gaitameSym, gaitameB, gaitameS, gaitameFound = gaitame(requestSym)
oandaSym, oandaB, oandaS, oandaFound = oanda(requestSym)
xmSym, xmB, xmS, xmFound = xm(requestSym)
moneySym, moneyB, moneyS, moneyFound = money(requestSym)
minfxSym, minfxB, minfxS, minfxFound = minfx(requestSym)

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

	print "------- マネパ -------"
	count = 0
	for o in moneySym:
		print o
		print "B:",moneyB[count]
		print "S:",moneyS[count]
		count = count + 1
	
	print "------- みんなのFX -------"
	count = 0
	for o in minfxSym:
		print o
		print "B:",minfxB[count]
		print "S:",minfxS[count]
		count = count + 1

def disp(requestSym):
	# 代入してからじゃないとエラー
	oanda = oandaFound - 1
	xm = xmFound - 1
	gaitame = gaitameFound - 1
	money = moneyFound
	minfx = minfxFound - 1
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

	print "------- マネパ -------"
	print moneySym[money]
	print "B:",moneyB[money]
	print "S:",moneyS[money]

	print "------- みんなのFX -------"
	print minfxSym[minfx]
	print "B:",minfxB[minfx]
	print "S:",minfxS[minfx]

if requestSym is "All":
	disp_all()
else:
	disp(requestSym)
