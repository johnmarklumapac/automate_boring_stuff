import re

hi = input('Enter somthing:')

phoneNumberRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
mo = phoneNumberRegex.search(hi)
print(mo.group())