#! /usr/local/bin/python

file = open('case4.out','r')
out1 = open('massflow.txt','w')
out2 = open('outletmass.txt','w')
out3 = open('fsflux.txt','w')
import re
import numpy as np

data = file.readlines()
file.seek(0)

time = []
opening = []
bund_nw = []
bund_ne = []
bund_se = []
bund_sw = []


for i in range(len(data)):
    t = file.readline()
    l = re.match("\W.*t=   ([^\s]+)",t)
    m = re.match("\W.*Vol.*opening[^:]* = \D(.*)",t)
    n = re.match("\W.*Vol.*bund-nw[^:]* = \D(.*)",t)
    o = re.match("\W.*Vol.*bund-ne[^:]* = \D(.*)",t)
    p = re.match("\W.*Vol.*bund-se[^:]* = \D(.*)",t)
    r = re.match("\W.*Vol.*bund-sw[^:]* = \D(.*)",t)

    if l:
        time.append(float(l.group(1)))
        #out2.write(l.group(1))
        #out2.write('   ')
  #      out3.write(l.group(1))
 #       out3.write('   ')
    if m:
        opening.append(abs(float((m.group(1)))))
        
    if n:
 #       tt = float(n.group(1))*_1.0
        bund_nw.append(abs(float(n.group(1))))
#        out1.write('	')
    if o:
        bund_ne.append(abs(float(o.group(1))))
        #out1.write('	')
    if p:
        bund_se.append(abs(float(p.group(1))))
        #out1.write('	')
    if r:
        bund_sw.append(abs(float(r.group(1))))
        #out1.write('	')



time = np.array(time)
opening = np.array(opening)
bund_nw = np.array(bund_nw)
bund_ne = np.array(bund_ne)
bund_se = np.array(bund_se)
bund_sw = np.array(bund_sw)

print NO_1
i = 0
print time[30000]
while True:
	print i
	if i < len(time):
		out1.write(str(time[i])+',')
		out1.write(str(opening[i])+',')
		out1.write(str(bund_nw[i])+',')
		out1.write(str(bund_nw[i])+',')
		out1.write(str(bund_se[i])+',')
		out1.write(str(bund_sw[i])+'\n')
		
		i = i+1
	else:
		break
print len(time)
file.close()
out1.close()
out2.close()
out3.close()
