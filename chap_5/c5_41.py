
import c5_40 as p40


class Chunk():
    def __init__(self,morphs,dst,srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs



def chunk_reader(file):
    sentence = []
    morph = []
    dep = []
    sentences = []
    morphs = []
    n = 0 #flag
    for line in file:
        if line == 'EOS\n': # for countinuous EOS
            if n != 0:
                chunk = Chunk(morphs,dep[2].strip('D'),dep[1])
                sentence.append(chunk)

            sentences.append(sentence)
            sentence = []
            morphs = []
            n = 0
        elif line[0] == "*" and n == 0:
            dep = line.split()
            n = 1
            continue
        elif line[0] == "*" and n != 0:
            chunk = Chunk(morphs,dep[2].strip('D'),dep[1]) #previous stem info
            dep = line.split()
            morphs = []
            sentence.append(chunk)
        else:
            surface, feature = line.split("\t")
            features = feature.split(",")
            morph = p40.Morph(surface,features[6],features[0],features[1])
            morphs.append(morph)

    return sentences


def main():
    with open('neko.txt.cabocha','r') as cabochafile:
        sentences = chunk_reader(cabochafile)

    return sentences

if __name__ == '__main__':
    sentences = main()
    for i, chunk in enumerate(sentences[7]):
        surfaces = ""
        for morph in chunk.morphs:
            print(morph.surface)
            surfaces += morph.surface

        print("%d:" % i, surfaces, "=>", chunk.dst)
