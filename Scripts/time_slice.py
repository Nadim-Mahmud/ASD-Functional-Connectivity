import nibabel as nb

img = nb.load("mri_bold.nii")

print(img.shape)
print(img.header)