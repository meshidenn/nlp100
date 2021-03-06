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
        noun = ''
        nv = ''
        buf = {}
        case = {}
        value = [[],[]]
        print("{}th sentence".format(i))
        for chunk in sentence:
            surface = ''
            n = 0
            if int(chunk.dst) == -1:
                k=0
            else:
                k=int(chunk.dst)

            for morph in chunk.morphs:
                surface += morph.surface
                
            for morph in chunk.morphs:
#                print(morph.surface,morph.base,morph.pos,morph.pos1)
                surfaces = []
                particles = []
                if morph.pos == '助詞' and morph.base != 'を':
                    particle = morph.base
                    m = 0
                    for morphv in sentence[k].morphs:
                        if morphv.pos == '動詞' and m == 0:
                            verb = morphv.base
                            surfaces.append(surface.strip())
                            particles.append(particle)
                            m = 1
                        else:
                            continue
                        if verb in buf: #value escape 
                            value = buf[verb]
                        buf[verb] = [[],[]]
                        print(surfaces,particles)
                        for key,val in buf.items():
                           if key == nv:
                               value[0] = sorted(particles)
                               value[1] = sorted(surfaces,key = lambda surfaces:surfaces[-1])
                               buf[verb] = value
                               value = [[],[]]

def func_verb(sentences,cases):
    for i, case in enumerate(caces):
        surfaces = []
        particles = []
        noun = ''
        nv = ''
        buf = {}
        case = {}
        value = [[],[]]
        print("{}th sentence".format(i))
                       
            for morph in chunk.morphs:
                if morph.pos == '名詞' and morph.pos1 == 'サ変接続':
                    noun = morph.base
                    n = 1
                    print('--noun--')
                    print(morph.surface,morph.base,morph.pos,morph.pos1)
                    print('---')
          
                if morph.base == 'を' and morph.pos == '助詞' and n == 1:
                    print("--condition clear--")
                    print("---")
                    wo = morph.base
                    m = 0
                    for morphv in sentence[k].morphs:
                        if morphv.pos == '動詞' and m == 0:
                            verb = morphv.base
                            nv = noun + wo + verb
                            m = 1
#                            surfaces.append(surface.strip())
#                            particles.append(particle)
                            print(nv, buf)
                        if nv in case: #value escape 
                            value = case[nv]
                        if len(nv) != 0 and len(particles) != 0 and len(surfaces) != 0:
                            case[nv] = []                    
                        for key,val in case.items():
                           if key == nv:
                               value[0] = buf[verb][0]
                               value[1] = buf[verb][1]
                               case[nv] = value
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
    funcs = func_verb(sentences,cases)

    return funcs

if __name__ == '__main__':
    funcs = main()    
    print(funcs)
    n = len(funcs)
    for i,func in enumerate(funcs):
        for k,v in func.items():
            n = len(v)
            if i == 0:
                with open('case_pattern_3.txt','w') as f:
                    f.write('{}\t'.format(k))
                    for out in v:
                        print('\t'.join(out),file=f,end='\t')
                    print('\n',file=f,end='')
            else:
                with open('case_pattern_3.txt','a') as f:
                    f.write('{}\t'.format(k,v))
                    for out in v:
                        print('\t'.join(out),file=f,end='\t')
                    print('\n',file=f,end = '')
