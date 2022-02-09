import csv
from email import header

csv_file = open('pokemon.csv', 'r',encoding="utf-8")
f = csv_reader = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
print(header)
for row in f:
    print(row)