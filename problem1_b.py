
def InputHandler():
    pattern = open("pattern.txt", "r")
    P = "".join(pattern.readlines())
    raw = open("raw.txt", "r")
    T = "".join(raw.readlines())
    pattern.close()
    raw.close()
    return T, P



''' BF stands for brute force '''
def BF_string_match():
    T, P = InputHandler()
    n = len(T); m = len(P)
    returnlst = []
    for s in range(0, n-m):
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

