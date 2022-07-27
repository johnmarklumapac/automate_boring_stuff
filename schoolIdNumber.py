def schoolIdNumber(text):
    if len(text) != 9:
        return False
    for i in range(0, 2):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 8):
        if not text[i].isdecimal():
            return False
    return True

print('Is bla bla bla a school id number?')
print(schoolIdNumber('bla bla bla'))

print('Is 191-01923 a school id number?')
print(schoolIdNumber('001-01923'))


    
    