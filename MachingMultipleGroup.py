import re

inputText = input("")

phoneNumRegex = re.compile(r'(\d\d\d\d)-(\d\d\d)-(\d\d\d)')
mo = phoneNumRegex.search(inputText)

print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.group())
print(mo.groups())
