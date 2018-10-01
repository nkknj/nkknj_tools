import os, sys, glob
import scipy.io
import numpy as np
import pandas as pd

def extractROItimeseries(f):
	df=pd.DataFrame()
	matfile=scipy.io.loadmat(f)

	n_names=len(matfile['names'][0])
	for i in range(n_names):
		if matfile['names'][0][i][0][:5]=='atlas':
			ROIname=matfile['names'][0][i][0]
			df[ROIname]=np.array(matfile['data'][0][i]).reshape(-1)

	return df
			
inputdir=sys.argv[1]
outputdir=sys.argv[2]

pathlist=glob.glob(os.path.join(inputdir, 'ROI_*.mat'))

for path in pathlist:
	df=extractROItimeseries(path)
	df.to_csv(os.path.join(outputdir, os.path.basename(path)[:-4]+'.csv'))

