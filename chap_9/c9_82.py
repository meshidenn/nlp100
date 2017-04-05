import random


def mkcontext(line):
    stw = line.split()
    n = len(stw)
    pairs = []
    for i,w in enumerate(stw):
        d = random.randint(1,5)
        ctwl = []
        if i > d and n > i+d :
            print('in')
            for j in range(i-d,i):
                ctwl.append(stw[j])
            for j in range(i+1,i+d+1):
                ctwl.append(stw[j])
        elif d > i and i+d >= n:
            print('out')
            for j in range(0,i):
                ctwl.append(stw[j])
            for j in range(i+1,n):
                ctwl.append(stw[j])
        elif d > i:
            print('left out')
            for j in range(0,i):
                ctwl.append(stw[j])
            for j in range(i+1,i+d+1):
                ctwl.append(stw[j])
        elif i+d >= n:
            print('right out')
            for j in range(i-d,i):
                ctwl.append(stw[j])
            for j in range(i+1,n):
                ctwl.append(stw[j])
        
        ctws = '\t'.join(ctwl)
        pair = w + '\t' + ctws
        pairs.append(pair)

    return pairs


def main():
    with open('lemmatize_2.txt', 'r') as f:
        for i, line in enumerate(f):
            pairs = mkcontext(line)

            for pair in pairs:
                print(pair)
                if i == 0:
                    with open('context_2.txt','w') as g:
                        print(pair,file=g)
                else:
                    with open('context_2.txt','a') as g:
                        print(pair,file=g)

if __name__ == '__main__':
    main()
