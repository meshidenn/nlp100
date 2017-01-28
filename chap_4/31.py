

import c4_30_2 as p30

def verb_extractor(sentences):
    verbs = []
    for sentence in sentences:
        for line in sentence:
            if line['pos'] == '動詞':
                verbs.append(line['surface'])

    return verbs

def main():
    sentences = p30.main()
    verbs = verb_extractor(sentences)
    return verbs

if __name__ == '__main__':
    verbs = main()
    print(verbs)
    for verb in verbs:
        print(verb)
