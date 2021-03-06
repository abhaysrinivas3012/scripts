import xlsxwriter
workbook = xlsxwriter.Workbook('pressure.xlsx')
out = open('tp.csv','w')
inp = open('input.dat','r')
ht = open('heights.dat','r')
case_name = 'case4_'
series = inp.readlines()

import os
import re
time = []
pres = []
sensor_id = []
max_pres = []
hts = []
max_pres_time = []
headings = ['time(s)','Pressure(Pa)','pmax','times']
numbers = re.compile(r'(\d+)')
def numericalSort(value):
	parts = numbers.split(value)
	parts[1::2] = map(int,parts[1::2])
	return parts

headings2 = ['Sensors ID', 'Times(s)', 'Height(m)','Maximum(Pa)']
worksheet1 = workbook.add_worksheet("Pmaximum")
worksheet1.write_row('A1',headings2)

for i in range(len(series)):
	p1 = series[i]
	ids = p1.split(',')
	for j in range(1,len(ids)):
		sensor_id.append(int(ids[j]))
worksheet1.write_column('A2',sensor_id)

h = ht.readline()
h = h.split(',')
for i in range(len(h)):
	hts.append(h[i])	

###Adding and plotting charts	
###Series 1
for i in range(len(series)):
	line = series[i]
	line = line.strip('\n')
	series_names = line.split(',')
	sheet_name = series_names[0]
	c1 = case_name+series_names[1]+'.TP!$A$2:$A$30000'
	c2 = case_name+series_names[2]+'.TP!$A$2:$A$30000'
	c3 = case_name+series_names[3]+'.TP!$A$2:$A$30000'
	c4 = case_name+series_names[4]+'.TP!$A$2:$A$30000'
	c5 = case_name+series_names[5]+'.TP!$A$2:$A$30000'

	v1 = case_name+series_names[1]+'.TP!$B$2:$B$30000'
	v2 = case_name+series_names[2]+'.TP!$B$2:$B$30000'
	v3 = case_name+series_names[3]+'.TP!$B$2:$B$30000'
	v4 = case_name+series_names[4]+'.TP!$B$2:$B$30000'
	v5 = case_name+series_names[5]+'.TP!$B$2:$B$30000'

	print c5
	worksheet = workbook.add_worksheet(sheet_name)
	chart1 = workbook.add_chart({'type': 'scatter','subtype':'straight'})

	chart1.add_series({'name':	hts[0+i*5],
			   'categories':c1,
			   'values'    :v1,
			   })
	
	chart1.add_series({'name':	hts[1+i*5],
			   'categories':c2,
			   'values'    :v2,
			   })
		   
	chart1.add_series({'name':	hts[2+i*5],
			   'categories':c3,
			   'values'    :v3,
			   })
		   
	chart1.add_series({'name':	hts[3+i*5],
			   'categories':c4,
			   'values'    :v4,
			   })

	chart1.add_series({'name':	hts[4+i*5],
			   'categories':c5,
			   'values'    :v5,
			   })

	chart1.set_title({'name':sheet_name})
	chart1.set_x_axis({'name':'time(s)'})
	chart1.set_y_axis({'name':'Pressure(Pa)','min':0})
	worksheet.insert_chart('A1', chart1,{'x_scale':2,'y_scale':2})




directory = '.'
print directory,type(directory)
for root,dirs,files in os.walk(directory):
	for file in sorted(files,key=numericalSort):
		if file.endswith(".TP"):
			fname = file[:len(case_name)-1]+'_'+file[len(case_name)-1:]
			worksheet = workbook.add_worksheet(fname)
			f = open(file,'r')
			print fname
			size = len(f.readlines())
			f.seek(0)
			f.readline()
			t = []
			p = []
			for i in range(size-1):
				l = f.readline()
				l = l.strip('\n \t')
				l = l.replace('   ','  ')
				l1 = l.split('  ')
				t.append(float(l1[0]))
				p.append(float(l1[1]))
			maxp = [max(p)]
			max_pres.append(max(p))
			maxpt = [t[p.index(max(p))]]
			max_pres_time.append(t[p.index(max(p))])
			worksheet.write_row('A1',headings)
			worksheet.write_column('A2',t)
			worksheet.write_column('B2',p)
			worksheet.write_column('C2',maxp)
			worksheet.write_column('D2',maxpt)
			time.append(t)
			pres.append(p)			
			f.close()
print max_pres_time			
worksheet1.write_column('B2',max_pres_time)
worksheet1.write_column('D2',max_pres)			


print len(time),len(pres)
print len(time[0]),len(pres[0])
print pres[0][1]

out.close()
workbook.close()