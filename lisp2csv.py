#-*-coding:utf-8 -*-
import re
import numpy as np
import csv

# This script is simply used to transfomr original time-series dataset from lisp format to csv format
with open("../Data/chorales.lisp", "r") as lines:
    array = []
    for line in lines:
    	if line.strip():
        	array.append(line)

with open("../Data/chorales.csv", "rw+") as f:
	f.write("{t0}\t{t1}\t{t2}\t{t3}\t{t4}\t{t5}\t{t6}\n".format(t0="ID", t1="start_time", t2="pitch", t3="duration", t4="key_signature", t5="time_signature", t6="fermata"))
	for i in range(0, len(array)):
		chorale = np.asarray(re.findall(r'\b\d+\b', array[i])).astype("int")
		chorale[0] = i
		ID = chorale[0].tolist()
		st = chorale[1:len(chorale)-5:6].tolist()
		pitch = chorale[2:len(chorale)-4:6].tolist()
		dur = chorale[3:len(chorale)-3:6].tolist()
		keysig = chorale[4:len(chorale)-2:6].tolist()
		timesig = chorale[5:len(chorale)-1:6].tolist()
		fermata = chorale[6:len(chorale):6].tolist()
#		print(len(st),len(pitch),len(dur), len(keysig), len(timesig), len(fermata)) # length all same, nice dataset		
		f.write("{ID}\t{st}\t{pitch}\t{dur}\t{keysig}\t{timesig}\t{fermata}\n".format(ID=ID, st=st, pitch=pitch, dur=dur, keysig=keysig, timesig=timesig, fermata=fermata))
	f.close()


