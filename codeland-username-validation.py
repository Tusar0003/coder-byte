import re


def CodelandUsernameValidation(strParam):
    # code goes here
    if re.match('^[a-zA-Z0-9_]{4,25}$', strParam) and str(strParam)[0].isalpha and str(strParam)[-1] != '_':
        strParam = True
    else:
        strParam = False

    return strParam


# keep this function call here
print(CodelandUsernameValidation(input()))