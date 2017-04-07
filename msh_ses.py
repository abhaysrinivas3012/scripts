#! /usr/local/bin/python

import sys
inp = open(sys.argv[1],'r')
out = open("msh.ses","w")
cad = sys.argv[2]
d1 = []
d2 = []
d3 = []
p1 = []
p2 = []
p3 = []
inp.readline()
inp.readline()
inp.readline() #skip
bkl = inp.readline()
bkl = bkl.strip('\n')
blks = bkl.split(' ')
inp.readline() #skip
u = int(inp.readline())
inp.readline() #skip
v = int(inp.readline())
inp.readline()
w = int(inp.readline())
for i in range(u):
	inp.readline()
	d = int(inp.readline())
	d1.append(d)
	inp.readline()
	p = inp.readline()
	p1.append(p)
	i = i+1
for j in range(v):
	inp.readline()
	d = int(inp.readline())
	d2.append(d)
	inp.readline()
	p = inp.readline()
	p2.append(p)
	j = j+1
for k in range(w):
	inp.readline()
	d = int(inp.readline())
	d3.append(d)
	inp.readline()
	p = inp.readline()
	p3.append(p)
	k = k+1

tot = u*v*w
lvl = u*v
print tot
print lvl
print blks
vol_no = 1
z= 0
out.write('LOA,CAD\n'+cad+'\n')
while z<w:
	for l in range(lvl):
		if str(vol_no) not in blks:
			out.write("MSH,CRE,STR\n")
			out.write("VOL\n")
			out.write("    "+str(vol_no)+"\n")
			x = l%u
			y = l//u
		#print l
#	print x
#	print y
#	print z
			out.write("  "+str(d1[x])+"/"+str(d2[y])+"/"+str(d3[z])+"\n")
			out.write("KIN\n")
			out.write(str(p1[x])+str(p2[y])+str(p3[z])+"1.000000\n0\n")
		vol_no = vol_no+1
	z = z+1
out.write('Men')
inp.close()
out.close()
	
