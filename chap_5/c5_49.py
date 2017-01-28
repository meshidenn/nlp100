import c5_40 as p40
import c5_41 as p41
import c5_43 as p43
import c5_48 as p48
import csv

def noun_to_noun(sentences):
    npaths = []
    n2nss = []
    for i, sentence in enumerate(sentences):
        num = []
        npath = []
        n2ns = []
        print("{}th sentence".format(i))
        for j,chunk in enumerate(sentence):
            n = 0
            k = int(chunk.dst)
            for morph in chunk.morphs:
                if morph.pos == '名詞':
                    num.append(j)
                    while k != -1:
                        n = 1
                        num.append(k)
                        k = int(sentence[k].dst)
                    else:
                        break
            if len(num) != 0:
                npath.append(num)
            num = []
            
        nn = len(npath)
        for i,num in enumerate(npath):
            for j in range(i+1,nn):
                n2n = []
                n2n_path = ''
                src_set = set(num)
                tag_set = set(npath[j])
                matched_list = list(src_set & tag_set)
                match_min = min(matched_list)
                k = 0
                if match_min == npath[j][0]:
                    while num[k] < match_min:
                        surface = ''
                        for morph in sentence[num[k]].morphs:
                            if morph.pos == '名詞' and k == 0:
                                surface += 'X'
                            else:
                                surface += morph.surface
                        n2n.append(surface)
                        k += 1
                    else:
                        n2n.append('Y')
                    for char in n2n:
                        if char != 'Y':
                            n2n_path += char
                            n2n_path += ' -> '
                        else:
                            n2n_path += char

                else:
                    while num[k] < match_min:
                        surface = ''
                        for morph in sentence[num[k]].morphs:
                            if morph.pos == '名詞' and k == 0:
                                surface += 'X'
                            else:
                                surface += morph.surface
                        n2n.append(surface)
                        k += 1
                    for char in n2n:
                        if char != n2n[-1]:
                            n2n_path += char
                            n2n_path += ' -> '
                        else:
                            n2n_path += char
                    n2n_path +=  ' | '
                    n2n = []
                    k = 0
                    while npath[j][k] < match_min:
                        surface = ''
                        for morph in sentence[npath[j][k]].morphs:
                            if morph.pos == '名詞' and k == 0:
                                surface += 'Y'
                            else:
                                surface += morph.surface
                        n2n.append(surface)
                        k += 1
                    for char in n2n:
                        if char != n2n[-1]:
                            n2n_path += char
                            n2n_path += ' -> '
                        else:
                            n2n_path += char
                    n2n_path += ' | '
                    surface = ''
                    for morph in sentence[match_min].morphs:
                        surface += morph.surface
                    n2n_path += surface

                if len(n2n_path) != 0:
                    n2ns.append(n2n_path)
    
        n2nss.append(n2ns)  
    return(n2nss)


                        

def main():
    with open('neko.txt.cabocha','r') as cabochafile:
        sentences = p41.chunk_reader(cabochafile)

#    phrases = base(sentences)
    paths = p48.noun_path_to_root(sentences)
    n2nss = noun_to_noun(sentences)

    return n2nss

if __name__ == '__main__':
    n2nss = main()    
    for i, n2ns in enumerate(n2nss):
        for j,n2n_path in enumerate(n2ns):
            if i == 0 and j == 0:
                with open('path_n2n.txt','w') as f:
                    print('{}'.format(n2n_path),file=f)
            else:
                with open('path_n2n.txt','a') as f:
                    print('{}'.format(n2n_path),file=f)
