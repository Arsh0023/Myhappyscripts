#! python3
# csvsort.py
#sorts the CSV files into a seperate folder
import os,shutil,re
os.chdir(r'D:\Chrome downloads')
chrome_dwn = os.listdir(r'D:\Chrome downloads')
st_reg = re.compile(r'''(CMVOLT \d{8}\.CSV) | (CMVOLT_\d{8}\.CSV) '''
	,re.VERBOSE)
for files in chrome_dwn:
	mo = st_reg.search(files)   #filename.endswith('string')
	if bool(mo) == True:
		shutil.move(files,r'D:\Chrome Sorted\CSV')