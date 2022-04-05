import os

for data in os.listdir('olin'):
    
    path = 'timeseries/olin/'+data.replace('.nii.gz', '')
    #print(path)
    if not (os.path.exists(path)):
   	 os.mkdir(os.path.join(path))
    
    for roi in os.listdir('atlas'):
   	 cmd = '3dmaskdump'+' -noijk'+' -xyz'+' -mask '+os.getcwd()+'/atlas/'+roi+' '+os.getcwd()+'/olin/'+data+' > '+path+'/'+data.replace('.nii.gz', '-')+roi.replace('.nii', '.csv')
   	 #print(cmd)
   	 os.system(cmd)