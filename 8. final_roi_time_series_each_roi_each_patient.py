import numpy as np
import pandas as pd
import os

VOXEL_PATH = r'D:/Project/Data/Practice/roi_voxels/'
PATH = r'D:/Project/Data/RoiSignal/roi_signal/'
OUT = r"D:/Project/Data/Practice/timeseries_roi/"


def mkdir_if_not_exists(path):
	if(not(os.path.exists(path))):
		os.mkdir(path)


def intersect_voxels(roi_path, sub_roi_path, out_dest):

	# roi_path = VOXEL_PATH + 'AngularGyrus.csv'
	roi_voxels = pd.read_csv(roi_path)
	# print(roi_voxels)

	cols = ['x', 'y', 'z'] + list(range(1, 211))
	# sub_roi_path = r'D:\Project\Data\RoiSignal\roi_signal\A00032284\A00032284-AngularGyrus.csv'
	sub_data = pd.read_csv(sub_roi_path, sep=' ', names=cols)

	merged_df = pd.merge(sub_data, roi_voxels, how='inner', on=['x', 'y', 'z'])

	drop_cols =  ['id', 'count']
	merged_df = merged_df.drop(np.arange(151, 211), axis=1)
	merged_df = merged_df.drop(drop_cols, axis=1)

	# print(merged_df.head)
	# print(merged_df.columns)
	merged_df.to_csv(out_dest, encoding='utf-8', index=False)

# roi_path = VOXEL_PATH + 'AngularGyrus.csv'
# sub_roi_path = r'D:\Project\Data\RoiSignal\roi_signal\A00032284\A00032284-AngularGyrus.csv'
# out_dest = r'D:\Project\Data\Practice\test.csv'
# intersect_voxels(roi_path, sub_roi_path, out_dest)


for sub in os.listdir(PATH):
	sub_path = PATH + sub + '/'
	print(sub_path)
	for sub_roi in os.listdir(sub_path):

		roi_name = sub_roi.split('-', 1)[1]
		
		# create folder if not exists
		folder_name = roi_name[:-4]
		folder_path = OUT + folder_name
		mkdir_if_not_exists(folder_path)

		print(sub_roi)
		sub_roi_path = sub_path + sub_roi
		# print(sub_roi_path)

		# roi voxels after union
		roi_name = sub_roi.split('-', 1)[1]
		roi_path = VOXEL_PATH + roi_name
		# print(roi_path)

		out_dest = OUT + folder_name + '/' + sub + '.csv'
		# print(dest_file)
		# print("\n")
		intersect_voxels(roi_path, sub_roi_path, out_dest)
