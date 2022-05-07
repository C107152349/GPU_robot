def encode(string):
    '''
    將輸入的字串進行編碼
    '''
    e = ""
    for s in string:
        e = e + (chr(ord(s) + 1))
    return e
def decode(string):
    '''
    將輸入的字串進行解碼
    '''
    d = ""
    for s in string:
        d = d + (chr(ord(s) - 1))
    return d