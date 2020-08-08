#!python3
#stocks.py
#will modify csv files 

import os,re,csv
import pandas as pd
os.chdir(r'D:\Chrome downloads')
st_reg = re.compile(r'''(CMVOLT \d{8}\.CSV) | (CMVOLT_\d{8}\.CSV) '''
	,re.VERBOSE)
plist = os.listdir() 
for files in plist:
	if bool(st_reg.search(files)) == True:
		csvfile = files
		#print(csvfile)
if bool(csvfile) == False:
	print("No related CSV files found")

#code above this just to find the csv file.
#is able to locate the desired CSV file.	
csvfile = pd.read_csv(csvfile)
#opening file correctly.
csvfile.drop(['Date','Underlying Previous Day Close Price (B)','Underlying Log Returns (C) = LN(A/B)','Previous Day Underlying Volatility (D)'],axis = 1, inplace = True)
#deleting columns perfectly.
#print(csvfile)
#df.to_csv(address) for saving the file.
#csvfile.to_csv(r'C:\Users\Arsh\Desktop\STOCKS.csv')
#csvfile.to_csv(r'C:\Users\arsha_us1v27x\Desktop')
nifty = pd.read_csv('Nifty50.csv')
#print(nifty)
result = csvfile.merge(nifty,on = 'Symbol')
net = result.sort_values(by = 'Current Day Underlying Daily Volatility (E) = Sqrt(0.94*D*D + 0.06*C*C)', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
net.to_csv(r'C:\Users\Arsh\Desktop\STOCKS.csv')
net.to_csv(r'C:\Users\arsha_us1v27x\Documents\STOCKS.csv')
os.system("pause")