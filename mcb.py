#! python3
#mcb.py 
#saves multiple lines of  data
#mcb save file name - to save the file.
#mcb filename - to call it back.
import sys,os,shelve,pyperclip
os.chdir(r'D:\Python\mcb.saved_data')
##this is for the saving one
file = shelve.open('mcb_data')
if len(sys.argv) == 3:
	file[sys.argv[2]] = pyperclip.paste() 
	file.close()
	mcb_keys = open(r'C:\Users\Arsh\Desktop\mcb_data keys.txt','a') #opening mcb keys in the append mode so that when it does not overwrites and adds a new key
	mcb_keys.write('\n'+sys.argv[2])
	mcb_keys.close()
	print('key - '+sys.argv[2]+' has been added to mcb key values')
	print('The data has been saved under the name '+ sys.argv[2])
elif len(sys.argv) == 2:
	if bool(file[sys.argv[1]]) == True:
		pyperclip.copy(file[sys.argv[1]])
		print('contents under '+sys.argv[1]+' have been copied to clip board')
	else:
		print('file with no such name exists')