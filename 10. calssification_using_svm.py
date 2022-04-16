import pandas as pd
import os 
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import random
import numpy as np

INPUT_PATH = 'D:/Project/Data/RoiSignal/time_series_after_flatening/'
META_PATH = 'D:/Project/Data/RoiSignal/subjects_meta.csv'


meta_data = pd.read_csv(META_PATH)


def svm_on_roi(roi_name, result_list):

    # roi_name = 'AngularGyrus.csv'
    roi_path = INPUT_PATH + roi_name
    roi_data = pd.read_csv(roi_path)
    roi_data = roi_data.values

    np.random.shuffle(roi_data)

    # print(roi_data)

    catagories = []
    data = []
    for row in roi_data:
        # print(row[0])
        tmp_row = meta_data.loc[meta_data['Anonymized ID'] == row[0]].values
        cat = 0 if tmp_row[0][2] == 'PATIENT' else 1
        catagories.append(cat)
        data.append(row[1:])
        

    # print(catagories)
    # print(data)

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(data, catagories, test_size=0.15,random_state=109)



    clf = svm.SVC(kernel='linear') # Linear Kernel
    clf.fit(X_train, y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

    print('ROI name : {}   -------------------------------------------------------'.format(roi_name))
    # Model Accuracy: how often is the classifier correct?

    ac = metrics.accuracy_score(y_test, y_pred)
    pc = metrics.precision_score(y_test, y_pred)
    rc = metrics.recall_score(y_test, y_pred)

    print("Accuracy:",ac)

    # Model Precision: what percentage of positive tuples are labeled as such?
    print("Precision:",pc)

    # Model Recall: what percentage of positive tuples are labelled as such?
    print("Recall:",rc)   
    print("\n")

    tmp_list = [roi_name[:-4], ac, pc, rc]
    result_list.append(tmp_list)

    return result_list


# controlling
result_list = []
for roi in os.listdir(INPUT_PATH):
    result_list = svm_on_roi(roi, result_list)

cols = ['roi_name', 'accuracy', 'precision', 'recall']
out_result = pd.DataFrame(result_list, columns = cols)
file_name = 'each_roi_accuracy_linear.csv'
out_result.to_csv(file_name, encoding='utf-8', index=False)