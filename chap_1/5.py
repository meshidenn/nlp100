def ngram(char,n):
    gram = []
    l = len(char)
    for i in range(0,l-n+1):
        buf = ''
        for j in range(i,n+i):
            buf += char[j]
        gram.append(buf)

    print(gram)


s = 'I am an NLPer'
w = s.split()

ngram(s,2)
ngram(w,2)