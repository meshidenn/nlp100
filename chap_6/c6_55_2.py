from stanford_corenlp_pywrapper import CoreNLP


def eigen_exp(file):
    proc = CoreNLP(configdict={'annotators': 'tokenize,ssplit,post,ner'}, corenlp_jars=["/Users/hiroki/program/python/nlp100/chap_6/stanford-corenlp-full-2016-10-31/*"])
    for line in file:
        proc.parse_doc(line)


def main():
    with open('nlp_sentence.txt','r') with f:
        eigen_exp(f)

    return()

if __name__ == "__main__":
    main()

        
