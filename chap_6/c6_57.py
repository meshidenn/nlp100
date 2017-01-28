import re
import pydot

class Idword():
    def __init__(self,id,word):
        self.id = id
        self.word = word
    
def dependency(file):
    sentence = re.compile("\<\/sentence\>")
    governor = re.compile(r'<governor idx=(.+)?>(.+)?</governor>')
    dependent = re.compile(r'<dependent idx=(.+)?>(.+)?</dependent>')
    start = re.compile(r'<dependencies type="basic-dependencies">')
    end = re.compile(r"\<\/dependencies\>")
    couples = []
    couple = []
    for line in file:
        t = sentence.search(line)
        g = governor.search(line)
        d = dependent.search(line)
        s = start.search(line)
        e = end.search(line)
        if t:
            if len(couple) != 0:
                couples.append(couple)            
            couple= []
            flag = 0
            print(line)
        if s:
            flag = 1
            print(line)
        if e:
            flag = 0
            print(line)
        if g and flag == 1:
            gline1 = line.strip()
            gline2 = gline1.lstrip('(<governor idx=)')
            gline3 = gline2.rstrip("(\\<\\/governor\\>)")
            gline4 = gline3.split(">")
            print(gline4)
            word_gov = gline4[1]
            gline5 = gline1.lstrip(r"(<governor idx=)")
            gline6 = gline5.split('>')
            id_gov = gline6[0]
            print('g',id_gov,word_gov)
            gov = Idword(id_gov,word_gov)
        if d and flag == 1:
            dline1 = line.strip()
            dline2 = dline1.lstrip('^(<dependent idx=)')
            dline3 = dline2.rstrip('$(</dependent>)')
            dline4 = dline3.split('>')
            print(dline4)
            word_dep = dline4[1]
            dline5 = dline1.lstrip(r'\\<dependent idx\\=')
            id_dep = dline5.split('>')[0]
            dep = Idword(id_dep,word_dep)
            print('d',id_dep,word_dep)
            couple.append([word_gov,word_dep])

    return(couples)
            
def main():
    with open('nlp_sentence.txt.xml','r') as file:
        couples = dependency(file)
    
    return(couples)
    
if __name__ == '__main__':
    couples = main()
    for i, couple in enumerate(couples):
        nn = len(couple)
        print(i ,'th sentence')
        nets = []
        for j in range(nn):
            net = (couple[j][0], couple[j][1])
            nets.append(net)
        if len(couple) != 0:
            g=pydot.graph_from_edges(couple)
            g.write_jpeg('./graph_57/nets_graph_{}.jpg'.format(i), prog='dot')

