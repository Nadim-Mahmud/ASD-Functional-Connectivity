import os
import gzip
import shutil
from pandas import read_csv


SOURCE_PATH = "D:\Project\Data\RoiSignal"
DESTINITION_PATH = 'F:\TmpData'

universities = ['olin', 'pitt']


df = read_csv('5320_ABIDE_Phenotypics_20211225.csv')


i = 0

for university in universities:
    univ_path = SOURCE_PATH + '\\' + university
    for dir in os.listdir(univ_path):
        i = i + 1
        source_path = univ_path + '\\' + dir
        row = df.loc[df['Anonymized ID'] == dir].values
        destination_path = ""
        if(row[0][1] == 'CONTROL'):
            destination_path = DESTINITION_PATH + '\\control\\' + dir   
            #print(dir, 'control')
        else:
            destination_path = DESTINITION_PATH + '\\patient\\' + dir
            #print(dir, 'patient') 
        print('Copying {}/94... {} to {}'.format(i, source_path, destination_path))
        destination = shutil.copytree(source_path, destination_path)       

#destination = shutil.copytree('D:\Project\Data\RoiSignal\olin\A00032284', 'F:\TmpData\olin\A00032284') 
#print(destination)

print('Success!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')