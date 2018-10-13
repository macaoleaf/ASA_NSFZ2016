import os
import sys
sys.path.append("..")
import scipy.io as sio
import lib.str2list as lt
import lib.standarization as ln

# This script is used to further proocess data by standardaring and reconstructing 

filepath = "../data/chorales.csv"

# first normalize pitches
IDs, sts, pitchs, durs, keysigs, timesigs, fermatas = lt.str2list(filepath)
ln.standarization(pitchs, keysigs)

reconstruct_total_1 = [] # reconstruct data as array containing only array of pitch and duration  
reconstruct_total_2 = [] # reconstruct data as array containing only array of time and fermata
for i in range(0, len(IDs)):
	reconstruct_current_1 = []
	reconstruct_current_2 = []
	for j in range(0 ,len(pitchs[i])):
		reconstruct_current_1.append([pitchs[i][j], durs[i][j]])
		reconstruct_current_2.append([sts[i][j], fermatas[i][j]])
	reconstruct_total_1.append(reconstruct_current_1)
	reconstruct_total_2.append(reconstruct_current_2)

# Export data so that can load easily next time
sio.savemat("../data/recons1.mat",{'re_dict1':reconstruct_total_1})
sio.savemat("../data/recons2.mat",{'re_dict2':reconstruct_total_2})