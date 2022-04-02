import pandas as pd
import os

PATH = r'D:/Project/Data/Practice/top_ten_match/'
OUT = "D:/Project/Data/Practice/final_roi_timeseries/"


if(not(os.path.exists(OUT))):
    os.mkdir(OUT)

for roi in os.listdir(PATH):
    roi_path = PATH + roi + '/'
    print(roi + '... !!!')
    tmp = []
    marked_voxels = {}
    for patient in os.listdir(roi_path):
        file_path = roi_path + patient
        # print(file_path)
        patient_timeS = pd.read_csv(file_path)
        # print(patient_timeS)
        patient_timeS = patient_timeS.values
        for voxelS in patient_timeS:
            patient_id = voxelS[0]
            time_series = voxelS[5:]
            # print(patient_id)
            # print(time_series)
            if((voxelS[0] in marked_voxels)):
                # print("skipped!")
                continue
            marked_voxels[voxelS[0]] = 1
            tmp.append(time_series)

    roi_ts = pd.DataFrame(tmp)
    file_name = OUT + roi + '.csv'
    roi_ts.to_csv(file_name, encoding='utf-8', index=False)