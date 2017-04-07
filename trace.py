#! /usr/bin/python
## Script to read trace file
file = open('FLUTRACE','r')
out = open('p1.csv','w')

aa = file.readlines()


file.seek(0)

i = 0
while True:
	l = file.readline()
	i = i+1
	if l == "*DATA\n":
		break
	
cyci = []
time = []
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
p6 = []
p7 = []
p8 = []
p9 = []
p10 = []
p11 = []
p12 = []
p13 = []
p14 = []
p15 = []
p16 = []
p17 = []
p18 = []
p19 = []
p20 = []
p21 = []
p22 = []
p23 = []
p24 = []

print i
q = i

##Loop through whole file
while i <= len(aa)-1:
##Loop through all the lines written for each trace save
	while q <= i+47:
		p = file.readline()
		p = p.split(',')
		for ee in range(len(p)):
			cyci.append(float(p[ee]))
		q = q+1
##Append the values for the current time to the respective arrays. For the array index  time is always 0 the rest is the same as that in FLUTRACE
	time.append(cyci[0])
	p1.append(cyci[1])
	p2.append(cyci[7])
	p3.append(cyci[13])
	p4.append(cyci[19])
	p5.append(cyci[25])
	p6.append(cyci[31])
	p7.append(cyci[37])
	p8.append(cyci[43])
	p9.append(cyci[49])
	p10.append(cyci[55])
	p11.append(cyci[61])
	p12.append(cyci[67])
	p13.append(cyci[73])
	p14.append(cyci[79])
	p15.append(cyci[85])
	p16.append(cyci[91])
	p17.append(cyci[97])
	p18.append(cyci[103])
	p19.append(cyci[109])
	p20.append(cyci[115])
	p21.append(cyci[121])
	p22.append(cyci[127])
	p23.append(cyci[133])
	p24.append(cyci[139])
        cyci = []	
	i = i+48

for kk in range(len(p1)):
	out.write(str(time[kk])+','+str(p1[kk])+','+str(p2[kk])+','+str(p3[kk])+','+str(p4[kk])+','+str(p5[kk])+','+str(p6[kk])+','+str(p7[kk])+','+str(p8[kk])+','+str(p9[kk])+','+str(p10[kk])+','+str(p11[kk])+','+str(p12[kk])+','+str(p13[kk])+','+str(p14[kk])+','+str(p15[kk])+','+str(p16[kk])+','+str(p17[kk])+','+str(p18[kk])+','+str(p18[kk])+','+str(p20[kk])+','+str(p21[kk])+','+str(p22[kk])+','+str(p23[kk])+','+str(p24[kk])+'\n')
