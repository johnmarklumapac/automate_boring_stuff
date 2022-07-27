def isPhoneNumber(something):
    if len(something) != 12:
        return False
    for i in range(0, 3):
        if not something[i].isdecimal():
            return False
    if something[3] != '-':
        return False
    for i in range(4, 7):
        if not something[i].isdecimal():
            return False
    if something[7] != '-':
        return False
    for i in range(8, 12):
        if not something[i].isdecimal():
            return False
    return True

print('123-456-7890 is a phone number')
print(isPhoneNumber('123-456-7890'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))