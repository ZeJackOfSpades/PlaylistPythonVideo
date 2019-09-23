#coding:utf-8

import datetime

Dnow	=	datetime.date.today()
print(Dnow)
t1		=	datetime.time(23, 00, 46)
d1		=	datetime.datetime(2018, 12, 10, 14, 28, 00)
d2		=	datetime.datetime(2018, 12, 27, 14, 28, 00)

print(d1.year)
print(t1)
tNow 	= datetime.datetime.now()
print(tNow)
print("tNow :",tNow.day, tNow.hour, tNow.minute, tNow.year)
if d1 < d2:
	d3 = d2 - d1
	print(d3)
	print("d1 est le plus ancien que d2")

else:
	d3 = d1 - d2
	print(d3)
	print("d1 est le plus récent que d2")
#print(d1)








