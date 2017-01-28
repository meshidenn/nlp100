import c4_30_2 as p30
from collections import Counter

def main():
    sentences = p30.main()
    all_surface = []
    for sentence in sentences:
        for morpheme in sentence:
            all_surface.append(morpheme['base'])

    return Counter(all_surface)

if __name__ == '__main__':
    counter = main()
    for word, count in counter.most_common():
        print(word.strip(),count)
