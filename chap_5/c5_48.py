import c5_40 as p40
import c5_41 as p41
import c5_43 as p43
import csv

def noun_path_to_root(sentences):
    paths = []
    for i, sentence in enumerate(sentences):
        surfaces = []
        particles = []
        path = []
        noun = ''
        print("{}th sentence".format(i))
        for chunk in sentence:
            surface = ''
            n = 0
            k = int(chunk.dst)
            for morph in chunk.morphs:
                surface += morph.surface
                
            for morph in chunk.morphs:
                if morph.pos == '名詞':
                    while k != -1:
                        n = 1
                        surfaces.append((surface.strip(),morph.pos))
                        surface = ''
                        for to_morph in sentence[k].morphs:
                            surface += to_morph.surface
                        k = int(sentence[k].dst)
                    else:
                        if n == 1:
                            surfaces.append(surface.strip())
                        break
            if len(surfaces) != 0:
                path.append(surfaces)
            surfaces = []
        if len(path) != 0:
            paths.append(path)
    return(paths)


    
def main():
    with open('neko.txt.cabocha','r') as cabochafile:
        sentences = p41.chunk_reader(cabochafile)

#    phrases = base(sentences)
    paths = noun_path_to_root(sentences)

    return paths

if __name__ == '__main__':
    paths = main()    
    for i,path in enumerate(paths):
        for surfaces in path:
            if i == 0:
                with open('path.txt','w') as f:
                    for surface in surfaces:
                        if surface != surfaces[-1]:
                            print('{}->'.format(surface[0]),file=f,end='')
                        else:
                            print('{}'.format(surface[0]),file=f)
            else:
                with open('path.txt','a') as f:
                    for surface in surfaces:
                        if surface != surfaces[-1]:
                            print('{}->'.format(surface[0]),file=f,end='')
                        else:
                            print('{}'.format(surface[0]),file=f)
