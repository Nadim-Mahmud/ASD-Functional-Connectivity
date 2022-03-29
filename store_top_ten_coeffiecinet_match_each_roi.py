import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
import datetime
import sys

# catching warnings 
import warnings
warnings.filterwarnings("error")


class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")
   
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass    
sys.stdout = Logger()

# progress bar
def progress_bar(current, total, bar_length=20, progress='progress'):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'{progress}: [{arrow}{padding}] {int(fraction*100)}%', end=ending)

# coefficinet calculation----------------------------------------------
# adding extra column id to the dataframe
def add_id(df):
	ls = range(1,df.shape[0]+1)
	df.insert(0, "id", ls, True)
	return df

# returns a dictinary after adding new inside voxel count to the dictionary
def calculate_coef(patient, control, control_count_dct):

	if(not('id' in patient)):
		patient = add_id(patient)
	
	if(not('id' in control)):
		control = add_id(control)

	cols_range = 150	
	cnt = 0
	cn = 0
	coef = 0
	cols = ['id','x', 'y', 'z'] + list(range(1, cols_range+1))

	data1 = patient.to_numpy()
	data2 = control.to_numpy()

	for signal1, signal2 in zip(data1, data2):
		
		try:
			coef = np.corrcoef(signal1[4:cols_range], signal2[4:cols_range])[0, 1]
		except Exception as error:
			print('Error from cathed: {} {}'.format(coef, error))
			continue
		
		if(not(signal1[0] in control_count_dct)):
			control_count_dct[signal1[0]] = 0

		if(-0.5 < coef and coef < 0.5):
			cnt = cnt + 1
			control_count_dct[signal1[0]] += 1
		else:
			cn = cn + 1

	#print('Indside range : {} Outside range {}\n'.format(cnt, cn))

	return control_count_dct

def drop_column_in_range(df, left, right):
	#print(df)
	drop_list = [i for i in range(left, right)]
	df = df.drop(drop_list, axis = 1)
	return df


CONTROL = 'D:/Project/Data/RoiSignal/control/'
PATIENT = 'D:/Project/Data/RoiSignal/patient/'
TMP_ROI = 'D:/Project/Data/Practice/top_ten_match/'


# calculate and store a single patients roi to this specific roi of controls and store top then disimilaties
def single_patient_all_control(patient_path, patient_id):
	
	roi_name = patient_path.split('-', 1)[1]
	roi_path = TMP_ROI + roi_name[0:-4]

	# return if already exists
	final_output = roi_path + '/' + patient_id + ".csv"
	if(os.path.exists(final_output)):
		print('Already computed !')
		return
	
	#create a path if not exists
	if(not(os.path.exists(roi_path))):
		os.mkdir(roi_path)

	cols = ['x', 'y', 'z'] + list(range(1, 211))
	patient = pd.read_csv(patient_path, sep=' ', names=cols)

	control_count_dct = {}
	cnt = 0

	for contr in os.listdir(CONTROL):
		cnt += 1
		contr_path = os.path.join(CONTROL, contr)
		control_roi = contr_path + '/' + contr + '-' + roi_name
		
		#print('{}/43 coefficient of {}  with {} for - {}'.format(cnt, patient_id, contr, roi_name))
		progress_bar(cnt, 43, 70, 'Patient - ' + patient_id)

		contorl = pd.read_csv(control_roi, sep=' ', names=cols)
		control_count_dct = calculate_coef(patient, contorl, control_count_dct)
	
	control_count_list = []
	for key in control_count_dct:
		control_count_list.append([key, control_count_dct[key]])

	control_count_list = sorted(control_count_list, key=lambda x: (x[1],x[0]), reverse=True)

	#print(control_count_list[:10])

	top_ten = pd.DataFrame(columns = ['id'] + cols)
	top_ten_count = []
	cnt = 0

	for ls in control_count_list:
		cnt += 1
		tmp_df = patient.loc[patient['id'] == ls[0]]
		top_ten = pd.concat([top_ten, tmp_df])
		top_ten_count.append(ls[1])
		if(cnt >= 10):
			break

	# adding count to new row
	top_ten.insert(1, "count", top_ten_count, True)
	top_ten = top_ten.sort_values('id')
	top_ten = drop_column_in_range(top_ten, 151, 211)

	# saving top ten disimiliraties of an patient voxels
	file_name = roi_path + '/' + patient_id + ".csv"
	#print('Top ten disimilaraties for {}'.format(patient_id))
	top_ten.to_csv(file_name, encoding='utf-8', index=False)


# pat = "A00032299"
# path = PATIENT + pat + '/' + pat + '-AngularGyrus.csv'
# single_patient_all_control(path, pat)



# all patients angular 


skip_roi = ['JuxtapositionalLobuleCortex-formerlySupplementaryMotorCortex', 
'LateralOccipitalCortex-inferiordivision', 'LateralOccipitalCortex-superiordivision']

roi_file = open('roi.txt', 'r')
for roi in roi_file:
	
	roi = roi.strip()
	print('ROI : {} ------------------------------------------------------------------------'.format(roi[:-4]))
	
	if(roi[:-4] in skip_roi):
		print('skipped')
		continue


	cnt = 0
	start = 0
	end = 0

	for pat in os.listdir(PATIENT):
		path = PATIENT + pat + '/' + pat + '-' + roi
		cnt += 1
		dt = end - start
		total = datetime.timedelta(seconds = (dt * (50 - cnt)))
		dt = datetime.timedelta(seconds = dt)
		print('{}/50 ROI : {}            SPT: {} | EST: {}'.format(cnt, roi[:-4], dt, total))
		start = time.time()
		single_patient_all_control(path, pat)
		end = time.time()

