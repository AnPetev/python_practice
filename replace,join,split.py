def replace(source,old,new):
    res = []
    len_old = len(old)
    for i in range(0,len(source)):
        if source[i:i + len_old] == old:
            res.append(source[i:i + len_old])
            res = []
            res.append(source[0:i])
            res.append(new)
    return res
    
#print(replace('hello','lo','ko'))

def join_seperately(data,sep):
    res = []
    len_sep = len(sep)
    for i in range(0,len(data)):
        res.append(data[i:i + len_sep])
    for i in range(0,len(res)):
        res[i].append('=')

    return res

#print(join_seperately([1,2,3,4,5],'='))

def split(source,sep):
    res = []
    len_sep = len(sep)
    for i in range(0,len(source)):
        if source[i:i + len_sep] == sep:
            res.append(source[i + len_sep])
    return res

#print(split('a#b#c#d','#'))






