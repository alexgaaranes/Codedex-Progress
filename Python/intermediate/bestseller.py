import csv

with open('Bestseller - Sheet1.csv', 'r') as src:
    reader = csv.reader(src)

    src.readline()
    print("Book with highest sales:")
    highest = 0

    for row in reader:
         if int(row[4]) > highest:
             highest = int(row[4])
             bestbook = row

    print(bestbook)


with open('bestseller_info.csv', 'w') as src:
    writer = csv.writer(src)

    writer.writerow(bestbook)

