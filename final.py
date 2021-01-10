import csv
dataset_1 = []
dataset_2 = []
with open("DataSet1.csv","r")as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset_1.append(row)
with open("DataSet_2_sorted.csv","r")as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset_2.append(row)
headers_1 = dataset_1[0]
planet_data1 = dataset_1[1:]
headers_2 = dataset_2[0]
planet_data2 = dataset_2[1:]
headers = headers_1+headers_2
planet_data = []
for index,data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])
with open("final.csv","a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)