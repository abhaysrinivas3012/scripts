#! /usr/bin/python

file = open('NTOUT','r')
out1 = open('massflow.txt','w')
out2 = open('outletmass.txt','w')
out3 = open('fsflux.txt','w')
import re

data = file.readlines()
file.seek(0)


for i in range(len(data)):
    t = file.readline()
    l = re.match("\W.*bigit[^:]*=.*\D(\d+)",t)
    m = re.match("\W.*Mass.*INLET[^:]* = \D(.*)",t)
    n = re.match("\W.*Mass.*OUTLET[^:]* = \D(.*)",t)
    o = re.match("\W.*FS_FLU[^:]* = \D(.*)",t)
    if l:
        out1.write(l.group(1))
        out1.write('   ')
        #out2.write(l.group(1))
        #out2.write('   ')
        out3.write(l.group(1))
        out3.write('   ')
    if m:
        out1.write(m.group(1))
        out1.write('   ')
    if n:
        tt = float(n.group(1))*-1.0
        out1.write(str(tt))
        out1.write('\n')
    if o:
        out3.write(o.group(1))
        out3.write('\n')



file.close()
out1.close()
out2.close()
out3.close()
