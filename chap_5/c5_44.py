import c5_40 as p40
import c5_41 as p41
import pydot

def parse(sentences):
    couples = []
    n = len(sentences)
    for i in range(n):
        couple = []
        for j, chunk in enumerate(sentences[i]):
            surfaces = ""
            for morph in chunk.morphs:
                surfaces += morph.surface
            couple.append((j,surfaces,chunk.dst))
        couples.append(couple)

    return couples

def main():
    with open('neko.txt.cabocha','r') as cabochafile:
        sentences = p41.chunk_reader(cabochafile)

    couples = parse(sentences)

    return couples

if __name__ == '__main__':
    couples = main()    
    n = len(couples)
#    snet = []
    for i, couple in enumerate(couples):
        nn = len(couple)
        print(i ,'th sentence')
        nets = []
        for j in range(nn):
            if int(couple[j][2]) == -1:
                k = 0
            else:
                k = int(couple[j][2])
            net = (couple[j][1], couple[k][1])
            nets.append(net)

        if len(nets) != 0:
            g=pydot.graph_from_edges(nets)
            g.write_jpeg('./graph_44/nets_graph_{}.jpg'.format(i), prog='dot')
            
