import c4_30_2 as p30
import csv

def mk_set(sentence):
    buf = []
#    for sentence in sentences:
    for line in sentence:
        buf.append(line['base'])

    wset = set(buf)
                                             
    return wset

def w_dict(wset,sentence):
    wdict  = {}
    for word in wset:
        wdict[word] = 1
    return wdict

def w_freq(wdict,sentence):
    wfreq = {}
#    buf = []
    n = 0
    for k, v in wdict.items():
        n += 1
#        for sentence in sentences:
        for line in sentence:
            if line['surface'] == k:
                v += 1
        print(k,v,n)
        wfreq[k] = v

    return wfreq

def fsort(wfreq):
    swfreq = sorted(wfreq.items(),key=lambda x:x[1], reverse = True)

    return swfreq

     

def main():
    sentence = p30.sub()
    wset = mk_set(sentence)
    wdict = w_dict(wset,sentence)
    wfreq = w_freq(wdict,sentence)
    swfreq = fsort(wfreq)
    
    return swfreq

if __name__ == '__main__':
    freq = main()
    print(type(freq))
    with open('neko.txt.freq','w') as file:
        for x in freq:
            print(x[0],x[1])
            file.write('{},{}\n'.format(x[0].rstrip('\n'), x[1]))

    print(freq)
        
#    for noun in nouns:
#        print(noun)
