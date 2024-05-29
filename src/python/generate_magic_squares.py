import copy

iterations = 0

def get_squares(s = [[0,0,0],[0,5,0],[0,0,0]]):
    global iterations
    vals = set([val for row in s for val in row])
    if 0 not in vals:
        iterations+=1
        for i in range(2):
            if sum(s[i]) != 15:
                return None
        for j in range(2):
            if s[0][j] + s[1][j] + s[2][j] != 15:
                return None
        if s[0][0]+s[2][2] != 10:
            return
        if s[0][2] + s[2][0] != 10:
            return None
        #print("MS found",s)
        return copy.deepcopy(s)
    else:
        left = set(range(1,10)) - vals
        resList = []
        for i in range(3):
            for j in range(3):
                if s[i][j] == 0:
                    for n in left:
                        s[i][j] = n
                        res = get_squares(s)
                        if res:
                            if len(left) == 1:
                                resList.append(res)
                            else:
                                resList += res
                        s[i][j]=0
                    if len(resList) > 0:
                        return resList
                    return None
            

if __name__ == '__main__':
    s = [[0,0,0],[0,5,0],[0,0,0]]
    ms = get_squares()

    for s in ms:
        for row in s:
            print(row)
        print()
    print(iterations)
        
        
