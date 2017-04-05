import pprint
from collections import defaultdict

def mkdict(word_list):
    d = {}
    w = ' '.join(word_list[1:])
    d[word_list[0]] = (w,len(word_list))
    return d

def insert(trie, key, value):
    if key:
        first, rest = key[0], key[1:]
        print(first)
        if first not in trie:
            trie[first] = {}
        pprint.pprint(trie)
        insert(trie[first],rest,value)
    else:
        trie['value'] = value
           

def mk_nation_lemlist(f):
    nd = defaultdict()
    for line in f:
        wl = line.split()
        if len(wl) != 1:
            insert(nd,wl,len(wl))

    return nd


def lemmatizer(raw,lemlist):
    conv_list = []
    for line in raw:
        wlist = line.split()
        i = 0
        conv= []
        n = len(wlist)
        while i < n:
            if wlist[i] in lemlist:
                con = []
                key = wlist[i]
                search = lemlist
                j = i
                while wlist[j] in key \
                      and wlist[j] != 'value':
                    val = search[wlist[j]]
                    key = list(val.keys())
#                    print(i,j,wlist[j],key)
                    con.append(wlist[j])
                    search = val
                    j += 1
                    if n <= j:
                        break
                j -= 1
                w = '_'.join(con)
                print(w)
                n = n - (j - i)
                wlist[i] = w
                k = i+1
                print(wlist)
                while k <= j:
                    wlist.pop(k)
                    j -= 1
                print(wlist)
            i += 1
        conv_list.append(wlist)
    return conv_list
        
def main():

    with open('nation_2.txt','r') as f:
        lemlist = mk_nation_lemlist(f)
        
        
    with open('proc_3.txt','r') as g:
        conv_list = lemmatizer(g,lemlist)

    return conv_list
        
if __name__ == '__main__':
    conv_list = main()

    with open('lemmatize_2.txt','w') as f:
        for conv in conv_list:
            out = ''
            for token in conv:
                out += token + ' '

            print(out,file=f)

