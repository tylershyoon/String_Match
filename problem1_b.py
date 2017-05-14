import codecs

def InputHandler():
    #pattern = codecs.open("pattern.txt", "r", "utf-8")
    pattern = open("pattern.txt","r")
    P = "".join(pattern.readlines())
    #raw = codecs.open("raw.txt", "r", "utf-8")
    raw = open("raw.txt", "r")
    T = "".join(raw.readlines())
    print (T)
    pattern.close()
    raw.close()
    return T, P

''' BF stands for brute force '''
def BF_string_match():
    T, P = InputHandler()
    n = len(T); m = len(P)
    returnlst = []
    for s in range(0, n-m+1):
        equal = True
        i = 0
        while equal is True and i<=(m-1):
            if T[s+i] != P[i]:
                equal = False
            else:
                i += 1
        if equal is True:
            returnlst.append(s)

    if len(returnlst) == 0:
        return ['NONE']
    else:
        return returnlst

def OutputHandler(lst):
    f = open("output.txt", "w")
    for index in lst:
        f.write(str(index))
        f.write(" ")

lst = BF_string_match()
OutputHandler(lst)

