with open ('f1.txt') as ff:
    data1=ff.read()

with open ('f2.txt') as sf:
    data2=sf.read()

data1+=data2

with open('merge.txt','w') as mf:
    mf.write(data1)