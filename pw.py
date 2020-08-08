#! python3
#pw.py - an insecure password manager
#sys.argv[0] is the name of the script
PASSWORDS = { "arsharsh239@gmail.com":"no no no bro",
             "blog":"doggymaster",
             "lugage":"1234",
             "1harneet278":"awholenewworldZayn12344",
             "jaswinderkaurr13@gmail.com":"qwerty1999",
             "WoWS":"wargaming",
             "desk":"r'C:\\Users\\Arsh\\Desktop\\",
             "fruits":"fruits = {'apple':'10','mango':'5','banana':'20','anar':'30'}"
}
import sys,pyperclip
if len(sys.argv) < 2:
	print("usage py.pw [account name]--> copy account password")
	sys.exit()

account = sys.argv[1] #by default system arguments are taken as strings
if len(sys.argv)==2:
	if account in PASSWORDS:
		pyperclip.copy(PASSWORDS[account])
		print("password for ",account,"is coppied to clipboard")
	else:
		print("password for this account is not saved")
#solve why dic is not updating taking system arguments #may be because it is passed as a value.
if len(sys.argv) == 3:
	dicup = {account:sys.argv[2]}
	PASSWORDS.update(dicup)
	print("the account has been saved successfully")