def morpheme_reader(mecabfile):
    sentences = []
    sentence = []
    for line in mecabfile:
        if line == 'EOS\n':
            sentences.append(sentence)
            sentence = []
        else:
            surface, feature = line.split("\t")
            features = feature.split(",")
            line_dict = {
                'surface': surface,
                'base': features[6],
                'pos': features[0],
                'pos1': features[1],
                }
            sentence.append(line_dict)


    return sentences

def morpheme_liner(mecabfile):
    sentence = []
    for line in mecabfile:
        if line == 'EOS\n':
            continue
        else:
            surface, feature = line.split("\t")
            features = feature.split(",")
            line_dict = {
                'surface': surface,
                'base': features[6],
                'pos': features[0],
                'pos1': features[1],
                }
            sentence.append(line_dict)


    return sentence

def main():
    with open("neko.txt.mecab", 'r') as mecabfile:
        sentences = morpheme_reader(mecabfile)
        
    return sentences

def sub():
    with open("neko.txt.mecab", 'r') as mecabfile:
        sentence = morpheme_liner(mecabfile)

    return sentence

if __name__ == '__main__':
    sentences = main()
    print("[")
    for sentence in sentences:
        print(sentence)
    print("]")
