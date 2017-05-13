# encoding: utf-8

import csv
import tmdb3
from itertools import izip
from collections import defaultdict
from tmdb3 import searchMovie
from tmdb3 import set_key
from tmdb3 import Movie
set_key('0cd9dbe8598f80a33a88e240373400fd')



'''
columns = defaultdict(list) # each value in each column is appended to a list

with open('movieTitle.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k
'''
imdbid = []
with open('imdb.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader) # Ignore first row

    for row in reader:
        imdbid.append(row[0])


j = 0
imdb_real=[]
name = []
res=[]
movyear=[]
genre=[]
director=[]
descriptions = []
image=[]
trailer = []
actor = []
for i in imdbid:

    try:
        res.append(Movie.fromIMDB(i))
    except Exception as e:
        continue
    '''
    try:
        res[j]
    except Exception as e:
        del res[-1]
        continue
    '''
    name.append(res[j].title)

    tempString=''
    for k in range(0,10):
        try:
            tempString+=res[j].posters[k].geturl()+'|'
        except Exception as e:
            break
    image.append(tempString)

    tempString=''
    for k in range(0,10):
        try:
            tempString+=res[j].cast[k].name+'|'
        except Exception as e:
            break
    actor.append(tempString)

    try:
        trailer.append(res[j].youtube_trailers[0].geturl())
    except Exception as e:
        del res[-1]
        del name[-1]
        del image[-1]
        del actor[-1]
        continue

    try:
        descriptions.append(res[j].overview)  # .encode('ascii','ignore'))
    except Exception as e:
        del res[-1]
        del name[-1]
        del image[-1]
        del actor[-1]
        del trailer[-1]
        continue

    try:
        director.append(res[j].crew[0].name)  # .encode('ascii','ignore'))
    except Exception as e:
        del res[-1]
        del name[-1]
        del image[-1]
        del actor[-1]
        del trailer[-1]
        del descriptions[-1]
        continue

    try:
        tempString=''
        for k in range(0, 5):
            try:
                tempString += res[j].genres[k].name + '|'
            except Exception as e:
                break
        genre.append(tempString)
    except Exception as e:
        del res[-1]
        del name[-1]
        del image[-1]
        del actor[-1]
        del trailer[-1]
        del descriptions[-1]
        del director[-1]
        continue

    try:
        movyear.append(res[j].releasedate.year)  # .encode('ascii','ignore'))
    except Exception as e:
        del res[-1]
        del name[-1]
        del image[-1]
        del actor[-1]
        del trailer[-1]
        del descriptions[-1]
        del director[-1]
        del genre[-1]
        continue

    try:
        imdb_real.append(i)  # .encode('ascii','ignore'))
    except Exception as e:
        del res[-1]
        del name[-1]
        del image[-1]
        del actor[-1]
        del trailer[-1]
        del descriptions[-1]
        del director[-1]
        del genre[-1]
        del movyear[-1]
        continue
    '''
    try:
        imdbid.append(res[j][0].imdb[2:])
    except Exception as e:
        del res[-1]
        del name[-1]
        del image[-1]
        del actor[-1]
        del trailer[-1]
        del descriptions[-1]
        continue
    '''
    '''
    except Exception as e:
        res.append('')
        name.append('BadData')
        image.append('')
        trailer.append('')
        descriptions.append('')
        imdbid.append('')
    '''
    j+=1

rows = zip(imdb_real, name, movyear, genre, director, actor, image, trailer, descriptions)

with open('test_out.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['imdbid', 'movname', 'movyear', 'genre', 'director', 'actor', 'image', 'trailer', 'descriptions'])
    for row in rows:
        try:
            writer.writerow(row)
        except Exception as e:
            continue