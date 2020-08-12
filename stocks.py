#!python3
#stocks.py
#will modify csv files 

import os,re,csv,requests,io
import datetime as dt
import pandas as pd

save_to_path = "C:\\Users\\{}\\Desktop\\".format(os.getlogin())
os.chdir(save_to_path)
stock_date = dt.date.today()

def dec_day():
	global stock_date
	dec = dt.timedelta(days=1)
	stock_date = stock_date - dec

#to_get csv files
while(True):
	try:
		p_date =  stock_date.strftime('%d%m%Y')
		daily_url = "https://www1.nseindia.com/archives/nsccl/volt/CMVOLT_{}.CSV".format(p_date)
		s=requests.get(daily_url)
		if(s.status_code == 404):
			raise Exception("Not a trading day :( ")
		s=s.content
		csvfile = pd.read_csv(io.StringIO(s.decode('utf-8')))

		nifty_url = "https://www1.nseindia.com/content/indices/ind_nifty50list.csv"
		s=requests.get(nifty_url).content
		nifty = pd.read_csv(io.StringIO(s.decode('utf-8')))
		break

	except:
		dec_day()

csvfile.to_csv(os.path.join(save_to_path,"{}.csv".format(p_date))) #df.to_csv(address) for saving the file.
csvfile.drop(['Date','Underlying Previous Day Close Price (B)','Underlying Log Returns (C) = LN(A/B)','Previous Day Underlying Volatility (D)'],axis = 1, inplace = True)
#deleting columns perfectly.
result = csvfile.merge(nifty,on = 'Symbol')
net = result.sort_values(by = 'Current Day Underlying Daily Volatility (E) = Sqrt(0.995*D*D + 0.005*C*C)', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
net.to_csv(os.path.join(save_to_path,"{}.csv".format(p_date))) #df.to_csv(address) for saving the file.
os.system("pause")