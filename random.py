import os,requests
words = requests.get(r"https://random-word-api.herokuapp.com/home/word?number=10")
print(words)
os.system("pause")