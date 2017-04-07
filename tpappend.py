#!/usr/bin/python

import os
import re

print os.getcwd()
numbers = re.compile(r'(\d+)')
def numericalSort(value):
	parts = numbers.split(value)
	parts[1::2] = map(int,parts[1::2])
	return parts
directory1 = "../set1" #directory where the first TP files are present 0-n. Path can be absolute path
directory2 = "./set2" #directory where the first TP files are present n-current

for root,dirs,files in os.walk(directory2):
	for file in sorted(files):	
		if file.endswith(".TP"):
			os.chdir(directory2)
			f = open(file,'r')
			a = file
			print a
			size = len(f.readlines())
			f.seek(0)
			f.readline()
			data2 = f.readlines()
			for root,dirs,files in os.walk(directory1):
				for file in sorted(files):
					if file == a:
						print 'here'
						os.chdir(directory1)
						f2 = open(file,'a')
						for i in range(len(data2)):
							f2.write(data2[i])
						f2.close()
			os.chdir('../')			
			f.close()


