import numpy as np
import pandas as pd
import os

MAIN = r"D:\Project\Data\Practice\A00032284"
REDUCED = r"D:\Project\Data\Practice\timeseries_roi"
PAT = "A00032284.csv"


red = []

for roi in os.listdir(MAIN):
    
    roi_name = roi.split('-', 1)[1]
    roi_name = roi_name[:-4]
    print(roi_name)

    before = MAIN + '\\' + roi
    after = REDUCED + '\\' + roi_name + "\\" + PAT
    
    bf = pd.read_csv(before)
    bf_count = bf.shape[0]
    
    af = pd.read_csv(after)
    af_count = af.shape[0]
    
    red.append([roi_name, bf_count, af_count, bf_count-af_count])


red = sorted(red, key=lambda x: (x[3],x[0]), reverse=True)


print(red)
cols = ['Region of Interest (ROI)', 'Voxel count before feature extraction', 'Voxel count after feature extraction', 'Difference']
res = pd.DataFrame(red)
res.to_csv('data reduction.csv', encoding='utf-8', index=False)


