import c4_30_2 as p30

def base_extractor(sentences):
    bases = []
    for sentence in sentences:
        for line in sentence:
            if line['pos'] == '動詞':
                bases.append(line['base'])

    return bases

def main():
    sentences = p30.main()
    bases = base_extractor(sentences)
    return bases

if __name__ == '__main__':
    bases = main()
    print(bases)
    for base in bases:
        print(base)

