
def read_file():
    fileObj = open('Animal.py')
    for line in fileObj:
        print(line)
    fileObj.close()

def safe_read():
    with open('Animal.py') as fileObj:
        for line in fileObj:
            print(line)

#read_file()
#safe_read()

def log():
    fileObj = open('log.txt', 'a')
    fileObj.write('this is my first line\n')
    fileObj.close()

def write_csv():
    data_records = [['rajesh', 'dev', 'python'], ['john', 'dev','java']]
    fp = open('dev_data.csv','w')
    for item in data_records:
        fp.write(",".join(item) + "\n")
    fp.close()

write_csv()

import csv
def read_csv():
    fp = open('dev_data.csv','r')
    data_records = csv.reader(fp, delimiter=',')
    for data in data_records:
        print(data)

read_csv()
    

log()
