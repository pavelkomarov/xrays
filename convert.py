import pydicom
from matplotlib import pyplot
import os

for fname in os.listdir('.'):
	if not fname.endswith('.py') and not fname.endswith('.png'):
		with pydicom.dcmread(fname) as dicom:
			pyplot.imsave(fname + '.png', dicom.pixel_array, cmap='bone')

