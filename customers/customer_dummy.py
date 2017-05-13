# encoding: utf-8

import csv
import tmdb3
from itertools import izip
from collections import defaultdict
from tmdb3 import searchMovie
from tmdb3 import set_key
from tmdb3 import Movie
set_key('0cd9dbe8598f80a33a88e240373400fd')

cusid=[]
cusname=[]
cusemail=[]
cuspassword=[]
cusPortraitUrl=[]

with open('cusid.csv', 'rb') as f:
    reader = csv.reader(f)

    for row in reader:
        cusid.append(row[0])
        cusname.append('default'+str(row[0]))
        cusemail.append('default'+str(row[0]+'@default.com'))
        cuspassword.append('default'+str(row[0]))
        cusPortraitUrl.append('https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwjN0tSugP3SAhWs5oMKHevTB5YQjRwIBw&url=http%3A%2F%2Fsx.xinhuanet.com%2Fsjyw%2F20160506%2F3112655_c.html&bvm=bv.151325232,d.amc&psig=AFQjCNE72cHUoor6RVt549fDHdRlIU42QQ&ust=1490921181771462')




rows = zip(cusid,cusname,cusemail,cuspassword,cusPortraitUrl)

with open('customers.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['cusid','cusname','cusemail','cuspassword','cusPortraitUrl'])
    for row in rows:
        try:
            writer.writerow(row)
        except Exception as e:
            continue