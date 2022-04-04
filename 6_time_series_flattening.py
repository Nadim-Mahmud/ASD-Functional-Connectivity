import pandas as pd
import os

IN_PATH = 'D:/Project/Data/Practice/timeseries_roi/'
OUT_PATH = 'D:/Project/Data/Practice/time_series_after_flatening/'



# flattend_roi_all_patient = []


# roi_name = 'AngularGyrus'
# roi_path = IN_PATH + roi_name
# patient = 'A00032284.csv'
# patient_path = roi_path + '/' + patient

# patient_ts = pd.read_csv(patient_path)
# patient_ts = patient_ts.values

# flatten = [patient[:-4]]
# for row in patient_ts:
#     flatten.extend(row[3:])

# flattend_roi_all_patient.append(flatten)

# print(flattend_roi_all_patient)
# print(len(flatten))

# flattend_roi_all_patient.append(flatten)

# roi_all_patient = pd.DataFrame(flattend_roi_all_patient)

# roi_all_patient.to_csv('test.csv', encoding='utf-8', index=False)


for roi in os.listdir(IN_PATH):
    roi_path = IN_PATH + roi
    flattend_roi_all_patient = []
    for sub in os.listdir(roi_path):
        sub_path = roi_path + '/' + sub

        patient_ts = pd.read_csv(sub_path)
        patient_ts = patient_ts.values

        flatten = [sub[:-4]]
        for row in patient_ts:
            flatten.extend(row[3:])
        flattend_roi_all_patient.append(flatten)
    
    file_name = OUT_PATH + roi + '.csv'
    print(file_name)
    roi_all_patient = pd.DataFrame(flattend_roi_all_patient)
    roi_all_patient.to_csv(file_name, encoding='utf-8', index=False)
