import os
import sys
sys.path.append("..")
import lib

filepath = "../Data/chorales.csv"

# first normalize pitches
IDs, sts, pitchs, durs, keysigs, timesigs, fermatas = lib.str2list(filepath)
lib.standarization(pitchs, keysigs)

