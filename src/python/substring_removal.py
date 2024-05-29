def getMinLength(seq, min_dict={}):
    if seq in min_dict:
        return min_dict[seq]
    
    elif ("AB" not in seq) and ("BB" not in seq):
        min_dict[seq] = len(seq)
        return len(seq)
    
    else:
        minV = float('inf')
        for index in range(len(seq)-1):
            if seq[index:index+2] in ['AB', 'BB']:
                substr = seq[:index]+seq[index+2:]
                if substr in min_dict:
                    val = min_dict[substr]
                else:
                    val = getMinLength(substr, min_dict)
                    min_dict[substr] = val
                if val < minV:
                    minV = val
        min_dict[seq] = minV
        #print(min_dict)
        return minV

if __name__ == '__main__':
    print(getMinLength("BABBA"))
    print(getMinLength("BABB"))
    print(getMinLength("ABB"*10000))
