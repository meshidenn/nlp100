import c5_40 as p40

class Chunk():
    def __init__(self):
        self.morphs = []
        self.dist = -1
        self.srcs = []

    def __repr__(self):
        if self.morphs:
            surfs = [morph.surface for morph in self.morphs if morph.pos != '記号']
            return "".join(surfs)

    def include_pos(self, pos):
        return pos in [morph.pos for morph in self.morphs]

    def morphs_of_pos(self, pos):
        return [morph for morph in self.morphs if morph.pos == pos]

    def morphs_of_pos1(self, pos1):
        return  [morph for morph in self.morphs is morph.pos1 == pos1]

def chunk_reader(cabochafile):
    sentences = []
    sentence = []
    for line in cabochafile:
        if line == "EOS\n":
            for i, c in enumerate(sentence[:-1]):
                if c.dist != -1:
                    sentence[c.dst].srcs.append(i)

            sentences.append(sentence)
            sentence = []
        elif line[0] == "*":
            chunk = Chunk()
            chunk.dst = int(line.split(' ')[2].strip('D'))
            sentence.append(chunk)
        else:
            surface, feature = line.split("\t")
            features = feature.split(",")
            morph = p40.Morph(surface, features[6], features[0],features[1])
            sentence[-1].morphs.append(morph)

    return sentences

def main():
    with open("neko.txt.cabocha", 'r') as cabochafile:
        sentences = chunk_reader(cabochafile)

    return sentences

if __name__ == '__main__':
    sentences = main()
    print("---")
    for i, chunk in enumerate(sentences[7]):
        surfaces = ""
        for morph in chunk.morphs:
            surfaces += morph.surface

        print("%d:" % i, surfaces, "=>", chunk.dst)
