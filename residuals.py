#!/usr/bin/python


data = open('RESID.XYT','r')
z1 = open('residuals.csv','w')
i = 0
dd = data.readlines()
print len(dd)
iter = []
pres = []
velz = []
temp = []
data.seek(0)

line = 0

while line<=21:
    data.readline()
    line = line+1


while i < (len(dd)-22):
    l1 = data.readline()
    l1 = l1.split(',')
    iter.append(l1[0])
    pres.append(l1[3])
    l2 = data.readline()
    l2 = l2.split(',')
    velz.append(l2[0])
    temp.append(l2[2])
    i = i+2

z1.write('Iterations,Pressure,Velocity Z,Temperature')
z1.write('\n')
for k in range(len(iter)):
    z1.write(iter[k])
    z1.write(',')
    z1.write(pres[k])
    z1.write(',')
    z1.write(velz[k])
    z1.write(',')
    z1.write(temp[k])
    z1.write('\n')
z1.close
