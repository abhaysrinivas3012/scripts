#! /usr/bin/python

file = open('FLHISXYT','r')
target = open('history.csv','w')

dd = file.readlines()
print len(dd)
file.seek(0)

line = 0
while line <=37:
   file.readline()
   line = line+1

i = 0
cycles = []
maxtemp = []
avgtemp = []

while i < (len(dd)-38):
    l1 = file.readline()
    l1 = l1.split(',')
    cycles.append(float(l1[0]))
    l2 = file.readline()
    l3 = file.readline()
    l3 = l3.split(',')
    avgtemp.append(l3[-3])
    l4 = file.readline()
    l5 = file.readline()
    l5 = l5.split(',')
    maxtemp.append(l5[-3])
    print i
    i = i + 5

iter = []
for value in cycles:
    qq = value*50
    iter.append(qq)

target.write('Iterations,Max Temp,Avg Temp')
target.write('\n')
for k in range(len(iter)):
    target.write(str(iter[k]))
    target.write(',')
    target.write(maxtemp[k])
    target.write(',')
    target.write(avgtemp[k])
    target.write('\n')
target.close
