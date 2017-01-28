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
            phrase.append((j,base,pos1,chunk.dst))
        phrases.append(phrase)

    return phrases

def verb_particle(phrases):
    n = len(phrases)
    cases = []
    for i, phrase in enumerate(phrases):
        nn = len(phrase)
        case = {}
        value = []
        print("{}th sentence".format(i))
        for j in range(nn):
            if int(phrase[j][3]) == -1:
                k = 0
            else:
                k = int(phrase[j][3])
            if '動詞' in phrase[k][2]:
                a = phrase[k][2].index("動詞")
                verb = phrase[k][1][a]
                if '助詞' in phrase[j][2]:
                    b = phrase[j][2].index("格助詞")
                    particle = phrase[j][1][b]
                    print(verb, particle)
                    if verb in case: #value escape 
                        value = case[verb]
                    case[verb] = []                    
                    for key,val in case.items():
                       if key == verb:
                           value.append(particle)
                           case[verb] = value
                           value = []

        if len(case) != 0:
            cases.append(case)
            print(case)
    return(cases)

    
def main():
    with open('neko.txt.cabocha','r') as cabochafile:
        sentences = p41.chunk_reader(cabochafile)

    phrases = base(sentences)
    cases = verb_particle(phrases)

    return cases

if __name__ == '__main__':
    cases = main()    

    n = len(cases)
    for i,case in enumerate(cases):
        for k,v in case.items():
            if i == 0:
                with open('case_pattern.txt','w') as f:
                    f.write('{}\t'.format(k))
                    print('\t'.join(v),file=f)
            else:
                with open('case_pattern.txt','a') as f:
                    f.write('{}\t'.format(k,v))
                    print('\t'.join(v),file=f)
