import os
import sys
sys.path.append("..")
import lib.str2list as lt
import lib.standarization as ln

filepath = "../data/chorales.csv"

# first normalize pitches
IDs, sts, pitchs, durs, keysigs, timesigs, fermatas = lt.str2list(filepath)
ln.standarization(pitchs, keysigs)

