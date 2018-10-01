#-*-coding:utf-8 -*-
import csv
import numpy as np
import pandas as pd
import ast
from io import StringIO

# This script is used to transfer the string representation of list into list form, making it easier for future process
filepath = "../Data/chorales.csv"

def str2list(path):
	IDs = []
	sts = []
	pitchs = []
	durs = []
	keysigs = []
	timesigs = []
	fermatas = []


	with open("{path}".format(path=path), "r") as lines:
	    array = []
	    for line in lines:
	    	newline = line.split("\t")
	    	if newline[0] != "ID":
				IDs.append(int(newline[0]))
				sts.append(ast.literal_eval(newline[1]))
				pitchs.append(ast.literal_eval(newline[2]))
				durs.append(ast.literal_eval(newline[3]))
				keysigs.append(ast.literal_eval(newline[4]))
				timesigs.append(ast.literal_eval(newline[5]))
				fermatas.append(ast.literal_eval(newline[6]))
	return IDs, sts, pitchs, durs, keysigs, timesigs, fermatas

IDs, sts, durs, pitchs, keysigs, timesigs, fermatas = str2list(filepath)

