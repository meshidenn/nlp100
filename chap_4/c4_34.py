import c4_30_2 as p30

def no_extractor(sentences):
    nos = []
    buf = []
    count = 0
    for sentence in sentences:
        for line in sentence:
            if line['pos'] == '名詞' and count == 0:
                buf.append(line['surface'])
                count = 1
                continue
            if line['surface'] == 'の' and count == 1:
                buf.append(line['surface'])
                count = 2
                continue
            if line['pos'] == '名詞' and count == 2:
                buf.append(line['surface'])
                nos.append(buf)
                buf = []
                count = 0

            count = 0
            buf = []

    return nos

def main():
    sentences = p30.main()
    nos = no_extractor(sentences)
    return nos

if __name__ == '__main__':
    nos = main()
    print(nos)
    for no in nos:
        print(no)

