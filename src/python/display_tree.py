def draw_tree(n):
    if n == 1:
        return ["0"]
    elif n == 2:
        return ["  0  ",
                " / \ ",
                "0   0"]
    else:
        sub_tree = draw_tree(n-1)
        sub_l = len(sub_tree[0])
        l = sub_l*2+1
        n_space = max(1,(sub_l-1)//2)
        res = [sub_l*' '+'0'+sub_l*' ']
        for i in range(n_space):
            res.append((sub_l-i-1)*' '
                        +'/'
                        +(1+i*2)*' '
                        +'\\'
                        +(sub_l-i-1)*' ')
        for line in sub_tree:
            res.append(line+' '+line)
        return res

def main():
    out = draw_tree(4)
    for l in out:
        print(l)
main()
            
