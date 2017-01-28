import c5_40 as p40
import c5_41 as p41
import c5_43 as p43
import csv

def base(sentences):
    phrases = []
    n = len(sentences)
    for i in range(n):
        phrase = []
        for j, chunk in enumerate(sentences[i]):
            pos1 = []
            base = []
            for morph in chunk.morphs:
                if morph.pos != '記号':
                    pos1.append(morph.pos1)
                    base.append(morph.base)
                    surface.append(morph.surface)
            phrase.append((j,surface,base,pos1,chunk.dst))
        phrases.append(phrase)

    return phrases

def verb_particle_term(sentences):
    cases = []
    for i, sentence in enumerate(sentences):
        nn = len(sentence)
        surfaces = []
        particles = []
        case = {}
        value = [[],[]]
        print("{}th sentence".format(i))
        for chunk in sentence:
            surface = ''
            if int(chunk.dst) == -1:
                k=0
            else:
                k=int(chunk.dst)

            for morph in chunk.morphs:
                surface += morph.surface
#                psurface = strip(surface)
                
            for morph in chunk.morphs:
                if '格助詞' == morph.pos1:
                    particle = morph.base
                    for morph in sentence[k].morphs:
                        if morph.pos == '動詞':
                            verb = morph.base
                            surfaces.append(surface)
                            particles.append(particle)
                        else:
                           break

                        print(verb, particle,surface)
                        if verb in case: #value escape 
                            value = case[verb]
                        case[verb] = []                    
                        for key,val in case.items():
                           if key == verb:
                               value[0].append(particle)
                               value[1].append(surface.strip())
                               # using buf for safty because of danger of sort and safty of sorted
                               buf0 = value[0]
                               buf1 = list(set(value[1]))
                               print(buf0,buf1,value[0],value[1])
                               value[0] = sorted(buf0)
                               value[1] = sorted(buf1,key = lambda buf1:buf1[-1])
                               case[verb] = value
                               value = [[],[]]

        if len(case) != 0:
            cases.append(case)
            print(case)
    return(cases)

    
def main():
    with open('neko.txt.cabocha','r') as cabochafile:
        sentences = p41.chunk_reader(cabochafile)

#    phrases = base(sentences)
    cases = verb_particle_term(sentences)

    return cases

if __name__ == '__main__':
    cases = main()    

    n = len(cases)
    for i,case in enumerate(cases):
#        if i == 0:
#            with open('case_pattern_2.txt','w') as f:
#                print("{}th sentence".format(i),file=f)
#        else:
#            with open('case_pattern_2.txt','a') as f:
#                print("{}th sentence".format(i),file=f)
            
        for k,v in case.items():
            n = len(v)
            if i == 0:
                with open('case_pattern_2.txt','w') as f:
                    f.write('{}\t'.format(k))
                    for out in v:
                        print('\t'.join(out),file=f,end='\t')
                    print('\n',file=f,end='')
            else:
                with open('case_pattern_2.txt','a') as f:
                    f.write('{}\t'.format(k,v))
                    for out in v:
                        print('\t'.join(out),file=f,end='\t')
                    print('\n',file=f,end = '')
