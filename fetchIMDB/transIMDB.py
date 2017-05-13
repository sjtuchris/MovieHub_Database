# encoding: utf-8

import csv
from itertools import izip
from collections import defaultdict


imdbid = []
with open('movie.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader) # Ignore first row

    for row in reader:
        imdbid.append(row[0])
imdbid_str = []
j=0

for i in imdbid:
	imdbid_str.append('0'*(7-len(str(i)))+str(i))
	j+=1

reader = csv.reader(open('movie.csv', 'rb'))
headers = next(reader, None)
writer = csv.writer(open('movie_str.csv','wb'))
if headers:
	writer.writerow(headers)
j=0
for row in reader:
	writer.writerow([imdbid_str[j], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8]])
	j=j+1
