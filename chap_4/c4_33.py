import c4_30_2 as p30

def noun_s_extractor(sentences):
    nouns_s = []
    for sentence in sentences:
        for line in sentence:
            if line['pos'] == '名詞' and line['pos1'] == 'サ変接続':
                nouns_s.append(line['surface'])

    return nouns_s

def main():
    sentences = p30.main()
    nouns_s = noun_s_extractor(sentences)
    return nouns_s

if __name__ == '__main__':
    nouns_s = main()
    print(nouns_s)
    for noun_s in nouns_s:
        print(noun_s)

