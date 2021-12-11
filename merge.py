import csv
import os

file_path = './'
file_list = os.listdir(file_path)
rows = []
header = ['Name', 'ID', 'Mail']

# loop all files in current directory
for file in file_list:
    print(file)
    file_name = file_path + file
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            rows.append(row)
    f.close()

# create a new file named as new.csv
with open('./new.csv', 'w+', encoding='utf-8') as f:

    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(rows)
    f.close()