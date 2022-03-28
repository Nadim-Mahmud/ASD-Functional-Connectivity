
path = "D:\\Reasearch\\Data\\anatomy_data\\olin\\dicom\\allegra\\mmilham\\abide_28730\\A00032284\\352496274_session_1\\mprage_0001\\MPRAGE.nii.gz"

import os 
import gzip
import shutil

path1 = os.path.join("D:\\Reasearch\\Data\\tmp\\nadim", 'none')
os.makedirs(path1)

with gzip.open(path, 'rb') as f_in:
    with open('D:\\Reasearch\\Data\\tmp\\nadim\\none\\file.nii', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)