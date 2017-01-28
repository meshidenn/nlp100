import c4_30_2 as p30

def freq_counter(sentences):
    freq = []
    buf = []
    count = 0
    for sentence in sentences:
        for line in sentence:
            if count == 0:
                buf = [line['surface'],1]
                freq.append(buf)
                count = 1
                print("first")

            n = len(freq)
            nn = n -1
            print(n)
            for i in range(n):
                if freq[i][1] == line['surface']:
                    freq[i][2] += 1
                    break
                elif i == nn:
                    buf = [line['surface'],1]
                    freq.append(buf)
                    break
                                             
    return freq

def main():
    sentences = p30.main()
    freq = freq_counter(sentences)
    return freq

if __name__ == '__main__':
    freq = main()
    print(freq)
#    for noun in nouns:
#        print(noun)

