def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 2):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print(isPhoneNumber('blablabla'))

