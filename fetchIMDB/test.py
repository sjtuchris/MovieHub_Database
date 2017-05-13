import csv

makes = []
with open('imdb.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader) # Ignore first row

    for row in reader:
        makes.append(row[0])

print makes[10000]
