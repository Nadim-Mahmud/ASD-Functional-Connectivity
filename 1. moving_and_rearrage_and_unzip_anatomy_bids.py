import os
import gzip
import shutil

# change the link for each university
source = "D:\\Reasearch\\Data\\anatomy_data\\um\\dicom\\signa\\mmilham\\abide_28730"
destinition_root = "D:\\Reasearch\\Data\\Final_Raw_Data\\um\\"
destinition = ""
filename = ""


#################################   For Anatomical Data      ###########################################



# recursively accessing all data on from an university
for root, dirnames, files in os.walk(source): 
    for x in files: 
        
        # filtering only file that we want ends with gz
        if x.endswith('.gz'):
           
            # splitting the directories to separete anonamized names started with A00
            folders = root.split('\\') 
            for dir in folders:
                if dir.find('A0') != -1:
                    destinition = dir

            filename = files[0]
            
            # destinition directory creation
            path = os.path.join(destinition_root + destinition, 'anat')
            if os.path.exists(path):
                print('Path already exists!\n')
            else:
                os.makedirs(path)
            

            # decompressing zip from source to destinition
            anatomy_image_source = root +"\\"+ filename
            anatomy_image_destinition =  path + "\\" + "MPRAGE.nii"
            message = "decompressing... " + anatomy_image_source
            print(message)

            
            with gzip.open(anatomy_image_source, 'rb') as f_in:
                with open(anatomy_image_destinition, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)


print('\nSucessful !!!') 