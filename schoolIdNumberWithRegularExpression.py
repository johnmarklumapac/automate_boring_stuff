import re

phoneNumberRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
mo = phoneNumberRegex.search('1111-222-333 bla bla bla')
print(mo.group())