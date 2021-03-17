#! python3
import re, pyperclip

#Regex for phone numbers (+65 99999999, (+65) 99999999, (+65)9999 9999, 9999 9999)
phoneRegex = re.compile(r'((((\((\+)?\d{2})\))|((\+)?\d{2}))?(\s)?\d{4}(\s)?\d{4})')

#Regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9._+]+         #username
@                       #@ symbol
[a-zA-Z0-9._+]+         #domain name
''',re.VERBOSE)
#Get the text off the clipboard
text = pyperclip.paste()

#Extract email address and phone number from text
phone = phoneRegex.findall(text)
email = emailRegex.findall(text)

allPhone = []

for number in phone:
    allPhone.append(number[0])

#Copying result to the clipboard
result = '\n'.join(allPhone) + '\n' + '\n'.join(email)
pyperclip.copy(result)