import numpy as np
from pandas import read_csv
import os

# Base direcotory of  bids format data
FILE_PATH = 'D:\Project\Data\Final_Raw_Data' 
university_list = ['olin', 'pitt'] 


df = read_csv('5320_ABIDE_Phenotypics_20211225.csv')
outputfile = open('Ages.csv', 'w')

out = '{},{},{},{},{}\n'.format("University","Anonymized ID","Subject Type","AgeAtScan","Sex")
outputfile.write(out)

cnt = 0

for univ in university_list:
    path = FILE_PATH + "\\" + univ
    #print(path)
    for id in os.listdir(path):
        #print(id)
        row = df.loc[df['Anonymized ID'] == id].values
        if (row[0][1] == 'PATIENT'):
            cnt = cnt + 1
        out = '{},{},{},{},{}\n'.format(univ, row[0][0], row[0][1], row[0][7], row[0][8])
        print(out)
        outputfile.write(out)
        
print(cnt)


outputfile.close()