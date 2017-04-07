#! /usr/local/bin/python

p = open('points.dat','r')
c = open('curves.dat' ,'r')
file = open('geom.ses','w')

pp = p.readlines()
cc = c.readlines()
print len(pp)
print len(cc)
p.seek(0)
c.seek(0)
#print p.readline()
file.write('\n')
file.write('LIM WRK 8\n')
file.write('LIM PNT 1024\n')
file.write('LIM LIN 512\n')
file.write('LIM CRV 2048\nLIM PLN 1024\nLIM SUR 1024\nLIM VOL 1024\n')
file.write('###########POINT DATA########\n')
for i in range(len(pp)):
	l = p.readline()
	l1 = l.split('\t')
	file.write('CRE PNT DAT ('+l1[0]+','+l1[1]+','+str(float(l1[2]))+') ##pnt '+str(i+1)+'\n')
print 'i =',i
ii = i+1
p.seek(0)
file.write('########LVL 4###########\n')
for i in range(ii,ii+len(pp)):
	l = p.readline()
	l1 = l.split('\t')
	file.write('CRE PNT DAT ('+l1[0]+','+l1[1]+',12.95) ##pnt '+str(i+1)+'\n')

file.write('############CURVE DATA###########\n')	
for j in range(len(cc)):
	m = c.readline()
	m1 = m.split('\t')
	if len(m1) == 2:
		file.write("CRE CRV CSP PNT "+m1[0]+","+str(int(m1[1]))+" ##crv "+str(j+1)+'\n')
	if len(m1) == 3:
		file.write("CRE CRV ARC PNT "+m1[0]+","+m1[1]+","+str(int(m1[2]))+" ##crv "+str(j+1)+'\n')
print 'j= ',j
jj = j+1
c.seek(0)
file.write("###########LVL 2########\n")
for j in range(jj,jj+len(cc)):
	m = c.readline()
	m1 = m.split('\t')
	if len(m1) == 2:
		file.write("CRE CRV CSP PNT "+str(int(m1[0])+ii)+","+str(int(m1[1])+ii)+" ##crv "+str(j+1)+'\n')
	if len(m1) == 3:
		file.write("CRE CRV ARC PNT "+str(int(m1[0])+ii)+","+str(int(m1[1])+ii)+","+str(int(m1[2])+ii)+" ##crv "+str(j+1)+'\n')		
file.write('############Surfaces########\n')
c1 = 1
c2 = 196
c3 = 14
c4 = 183
while c1<=157:
	for k in range(13):
		file.write("CRE SUR DBL "+str((k*1)+c1)+','+str((k*13)+c2)+','+str((k*1)+c3)+','+str((k*13)+c4)+'  ## SUR '+str((k*1)+c1)+'\n')
	c1 = c1+13
	c2 = c2+1
	c3 = c3+13
	c4 = c4+1
print 'k = ',k
file.write("CRE SUR TRA 1-169 NOR [(0,0,0)(0,0,0.45)] 0 ##SUR 170-338\n")
file.write("CRE SUR TRA 1-169 NOR [(0,0,0)(0,0,0.75)] 0 ##SUR 339-507\n")
c1 = 365
c2 = 560
c3 = 378
c4 = 547
tt = 508
while c1<=521:
	for k in range(13):
		file.write("CRE SUR DBL "+str((k*1)+c1)+','+str((k*13)+c2)+','+str((k*1)+c3)+','+str((k*13)+c4)+'  ## SUR '+str(tt)+'\n')
		tt = tt+1
	c1 = c1+13
	c2 = c2+1
	c3 = c3+13
	c4 = c4+1
file.write("CRE SUR TRA 508-676 NOR [(0,0,0)(0,0,30.0)] 0 ##SUR 677-845\n")
file.write("###########VOLUMES###########\n")
for z in range(676):
	file.write("CRE VOL SLR "+str(z+1)+','+str(z+170)+'  ##VOL '+str(z+1)+'\n')
p.close
c.close
file.close
