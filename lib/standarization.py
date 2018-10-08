import numpy as np

# This script is used to adjust pitchs for each chorale accoding to their key signatures so that we can reduce data dimensions
def standarization(pitches, keysiges):
	for cindex in range(0, len(pitches)):
		offset = keysiges[cindex][0]
		pitches[cindex] = (np.asarray(pitches[cindex]) + offset).tolist()


