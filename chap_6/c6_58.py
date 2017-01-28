import sys
import xml.etree.ElementTree as ET
import re
from functools import partial

LRB = re.compile(r'-LRB- ')
RRB = re.compile(r' -RRB-')
NOTATION = re.compile(r' ([,\.:;])')
LDQ = re.compile(r'`` ')
RDQ = re.compile(r" \'\'")
SQ = re.compile(r" '")
SQS = re.compile(r" 's")

class StanfordDocument():

    def __init__(self,xmlfilename):
        self.xmltree = ET.parse(xmlfilename)

        root = self.xmltree.getroot()
        self.sentences = root.find('document/sentences')
        self.coreferences = root.find('document/coreference')

    def get_list_of_sentences(self):
        sentences = []
        for sentence in self.sentences.findall('sentence'):
            sentences.append([word.text for word in sentence.findall('tokens/token/word')])

        return sentences
        

def main(xmlfilename):
    doc = StanfordDocument(xmlfilename)
    sentences = doc.sentences.findall('sentence')

    dep_info = []
    dep_dic = {}
    dep_triples = []
    
    
    for i,sentence in enumerate(sentences):
        dep_triple = []
        dependency = sentence.find("dependencies[@type='collapsed-dependencies']")
        parse = sentence.find('parse')
        for dep in dependency:
            gov = (dep.find('governor').get('idx'), dep.find('governor').text)
            if dep.get('type') in ['nsubj','dobj']:
                dep_dic.setdefault(gov,[]).append((dep.get('type'), dep.find('dependent').text))

        verbs = [key for key, value in dep_dic.items() if set([t for (t,d) in value]) == set(['nsubj','dobj'])]

        for verb in verbs:
            nsubj = [d for (t,d) in dep_dic[verb] if t=='nsubj']
            dobj = [d for (t,d) in dep_dic[verb] if t =='dobj']
            print(nsubj,dobj)
            dep_triple += [[verb[1], n, d] for n in nsubj for d in dobj]

        dep_triples.append(dep_triple)

    print(dep_triples)

    return(dep_triples)

if __name__ == '__main__':
    dep_triples = main(sys.argv[1])
    for dep_triple in dep_triples:
        for v in dep_triple:
            print(v[1],'\t',v[0],'\t',v[2])
         
