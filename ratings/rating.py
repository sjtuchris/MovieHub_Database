import csv
from itertools import izip

f=open('ratings.dat.txt',"r")
lines=f.readlines()
result=[]
result.append(0)
j=0
for i in lines:
    result.append(i.split('::'))
    j+=1

custid=[]
imdbid=[]
ratings=[]
timestamp=[]
for i in result:
    try:
        custid.append(i[0])
        imdbid.append('0'*(7-len(str(i)))+str(i[1]))
        ratings.append(i[2])
        timestamp.append(i[3][:-1])
    except Exception as e:
        continue

rows = zip(custid, imdbid, ratings, timestamp)

with open('test_out.csv', 'wb') as f:
    writer = csv.writer(f)
    for row in rows:
        try:
            writer.writerow(row)
        except Exception as e:
            continue