import pickle
import sys

import numpy as np

import matplotlib.pylab as plt


#for line in infile:
#    print(line)
    #vals = line.split(',')
    #print(len(vals))
#


infilename = sys.argv[1]

values = np.loadtxt(infilename,dtype=str,unpack=True,skiprows=1,delimiter=',')
print(values[1])
print(len(values[1]))

infile = open(infilename,'r')
headers = infile.readline().split(',')

tmp = []
for h in headers:
    tmp.append(h.strip())

headers = tmp
print(headers)

# STORE ALL THE DATA BY THE HEADERS
allzipdata = {}
for h,v in zip(headers,values):


    if h=='Latitude' or h=='Longitude':
        allzipdata[h] = v.astype(float)
    elif h=='GMT':
        allzipdata[h] = v.astype(int)
    else:
        allzipdata[h] = v

# For plotting purposes only
#r = 6000
#x = r*allzipdata['Longitude']#*np.cos(allzipdata['Latitude'])
#y = r*allzipdata['Latitude']
#
#plt.figure()
#plt.plot(x,y,'.')

# Some places don't have a lat/lon. Mostly military places
# https://www.google.com/search?q=state+code+ae&ie=utf-8&oe=utf-8&client=firefox-b-ab
# AP, AE, etc.
idx = allzipdata['Latitude']==0.0
print(allzipdata['City'][idx],allzipdata['StateCode'][idx])

plt.show()

# Store by county 
counties = {}
zipinfos = {}
for z,c in zip(allzipdata['ZipCode'],allzipdata['MixedCounty']):

    countykeys = list(counties.keys())
    zipkeys = list(zipinfos.keys())

    if c not in countykeys:
        counties[c] = []
    else:
        counties[c].append(z)

    if z not in zipkeys:
        zipinfos[z] = []
    else:
        zipinfos[z].append(c)



#filename = "CARES_zipcode_data_v2.pkl"
filename = "CARES_zipcode_data_v3.pkl"
outfile = open(filename,'wb')
#
#pickle.dump([counties,zipinfos,allzipdata],outfile,1)
pickle.dump([counties,zipinfos,allzipdata],outfile,3)
outfile.close()
