import sys


def check_length(code):
    if len(code) <= 8:
        return False
    else:
        return True

def check_char(code):
    flag1, flag2, flag3, flag4 = 0, 0, 0, 0
    for i in code:
        if i.isupper():
            flag1 = 1
        elif i.islower():
            flag2 = 1
        elif i.isdigit():
            flag3 = 1
        else:
            flag4 = 1
    if (flag1+flag2 +flag3 +flag4) >= 3:
        return True
    else:
        return False

def check_str(code):
    for i in range(len(code)-3):
        if code.count(code[i:i+3]) > 1:
            return False
    return True


while True:
    try:
        s = raw_input()
        if check_length(s) and check_char(s) and check_str(s):
            print "OK"
        else:
            print "NG"
    except:
        break