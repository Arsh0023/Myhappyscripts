#!python3
#stocks.py
#will modify csv files 

import os,re,csv,requests
import datetime as dt
import pandas as pd
#need to replace all this with the requests one to download.
# https://www1.nseindia.com/archives/nsccl/volt/CMVOLT_11082020.CSV
save_to_path = "C:\\Users\\{}\\Desktop\\".format(os.getlogin())
os.chdir(save_to_path)
stock_date = dt.date.today()

def dec_day():
	global stock_date
	dec = dt.timedelta(days=1)
	stock_date = stock_date - dec
dec_day()
p_date =  stock_date.strftime('%m%d%Y')
print(p_date)

#to_get csv files
while(True):




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

# CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
# with requests.Session() as s:
#     download = s.get(CSV_URL)

#     decoded_content = download.content.decode('utf-8')

#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#     my_list = list(cr)
#     for row in my_list:
#         print(row)

csvfile = pd.read_csv(csvfile)
#opening file correctly.
csvfile.drop(['Date','Underlying Previous Day Close Price (B)','Underlying Log Returns (C) = LN(A/B)','Previous Day Underlying Volatility (D)'],axis = 1, inplace = True)
#deleting columns perfectly.
#df.to_csv(address) for saving the file.

#fix this to nifty 50 list online.
nifty = pd.read_csv('Nifty50.csv')
#print(nifty)
result = csvfile.merge(nifty,on = 'Symbol')
net = result.sort_values(by = 'Current Day Underlying Daily Volatility (E) = Sqrt(0.94*D*D + 0.06*C*C)', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
net.to_csv(os.path.join(save_to_path,"{}.csv".format(p_date)))
os.system("pause")