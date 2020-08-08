#! python3
# checks for phone numbers and mail and copies them to clip boards
import re,pyperclip 
phone_reg = re.compile(r'''\d{3}-\d{3}-\d{4}|
	\d{10}|
	\+91 \d+|
	\(\d{3}\)\(\d{7}\)

''',re.VERBOSE)
##now the text to search will be given as an argument.
#but before that create a regex for email
email_reg = re.compile(r'''[a-zA-Z0-9./+]+  #username
	@
	[a-zA-Z0-9]+
	\.[a-zA-z]{2,4}
''',re.VERBOSE)
#regex for websites
site_reg = re.compile(r'''(http)+|(https)+|(www\.)+|(:/|:/)?|
	[a-zA-Z0-9]+
	\.[a-zA-Z0-9]{2-4}

	''',re.VERBOSE)
#pyperclip.paste() gets the string values of the contents on the clip board.
text = str(pyperclip.paste())
phone = phone_reg.findall(text)
mail = email_reg.findall(text)
sites = site_reg.findall(text)
if bool(phone) == True:
	print("All the phone numbers have been successfully copied.")
else:
	print("No phone number was there")
if bool(mail) == True:
	print("All the emails have been successfully copied.")
else: 
	print("No email id was there")
if bool(sites) == True:
	print("All the sites have been successfully copied")
else:
	print("no sites were found.")
result = phone+mail+sites
pyperclip.copy(str(','.join(result)))