import re
import os

file = open("data.txt", "r")
txt = file.read()

def extraxtEmails(text): 
    return re.findall("[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+", text)

emails = extraxtEmails(text=txt)
print(emails)
file.close