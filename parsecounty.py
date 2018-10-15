#!/data/data/com.termux/files/usr/bin/env python
#parsecounty.py
counties=dict()

def parse(fl,listob=[]):
    """get csv representation as a list object with parse method by passing a csv file object."""
    
    with open(fl,'r') as fl:  
        for line in fl.readlines():
            entry=line.split(',')
            entry[-1]=entry[-1].replace('\n','')
            #pri nt(entry,"Length: ",len(entry))
            listob.append(entry)
        fl.close()
    return listob

#counties=parse('county.csv')
data=parse('subcounties.csv')
mapdf={}
def list2dict(listobj):
    """Create a key,value dict of county code to county or subcounties by passing a list of counties or a list of subcounties."""
    #if it's a list of counties, do
    for entry in listobj:
        counties[int(entry[0])]=entry[1]
    for i in range(1,48):
        mapdf[i]=list()
        for entry in listobj:
            if int(entry[0])==i:
                mapdf[i].append(entry[-1])

list2dict(data)
subcounties=mapdf
