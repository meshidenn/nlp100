import c4_30_2 as p30

def noun_extractor(sentences):
    nouns = []
    buf = []
    count = 0
    noun = ''
    for sentence in sentences:
        for line in sentence:
            if line['pos'] == '名詞':
                noun += line['surface']
            elif noun != '':
                nouns.append(noun)
                noun = ''
 
    return nouns

def main():
    sentences = p30.main()
    nouns = noun_extractor(sentences)
    return nouns

if __name__ == '__main__':
    nouns = main()
    print(nouns)
    for noun in nouns:
        print(noun)

