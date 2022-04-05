import pandas as pd
import os


# Stores cordinate which voxels remains after unions

PATH = r'D:/Project/Data/Practice/top_ten_match/'
OUT = "D:/Project/Data/Practice/roi_voxels/"


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
            coordinate = voxelS[:5]
            # print(patient_id)
            # print(coordinate)
            if((voxelS[0] in marked_voxels)):
                # print("skipped!")
                continue
            marked_voxels[voxelS[0]] = 1
            tmp.append(coordinate)

    cols = ['id', 'count', 'x', 'y', 'z']
    roi_coord = pd.DataFrame(tmp, columns=cols)
    roi_coord = roi_coord.sort_values('id')
    # print(roi_coord)
    file_name = OUT + roi + '.csv'
    roi_coord.to_csv(file_name, encoding='utf-8', index=False)