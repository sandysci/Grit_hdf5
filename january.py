import pandas as pd
import numpy as np
import datetime as dt
import time
import json
import h5py

with open('jsondata/january.json') as json_data:
    raw_data = json.load(json_data)

dictdata ={}
value = list()


currenttime = str(time.time())
currenttime = currenttime.replace(".", "")
hdf5filename = 'jan'+currenttime+'.h5'
csvfilename = 'jan'+currenttime+'.csv'
for key in raw_data:
	for c in key:		
		if c in dictdata:
			if type(key[c]) != unicode:
				# print str(key[c])
				dictdata[c].append(str(key[c]))
		else:
			if type(key[c]) != unicode:
				dictdata[c] = [str(key[c])]
# print dictdata
df =  pd.DataFrame(dictdata)

csvfile = df.to_csv('files/'+csvfilename)
#
file = h5py.File('files/'+hdf5filename,'w')
file.create_dataset("dset",(17, len(dictdata['Voltage3'])), 'f8')
file.close()
file2 = h5py.File('files/'+hdf5filename,'r+')

dataset2= file2['/dset']
# for c in dictdata.keys():
# 	dataset2.attrs[c] = c

# print dataset2.attrs

alldata = np.array(dictdata.values())
alldata2 = alldata.astype(np.float)
dataset2[...] = alldata2
file2.close()
