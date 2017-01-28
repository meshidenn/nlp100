import sys
import c6_58 as p58

class TreeParser():

    def __init__(self):
        self.root = None
        self._stack = [[]]

    def parse(self, tree_string):
        reading =  []
        for character in tree_string.strip():
            if character == '(':
                self._stack.append([])
            elif character == ' ':
                if reading:
                    self._stack[-1].append(''.join(reading))
                reading.clear()
            elif character == ')':
                if reading:
                    self._stack[-1].append(''.join(reading))
                reading.clear()
                self._stack[-2].append(self._stack.pop())
            else:
                reading.append(character)

                
        self.root = self._stack.pop()


    def get_phrase(self,tag):
        s = self.root[0][1]
        return self._recursive_finder(s, tag)

    def _recursive_finder(self, lst, tag):
        result = []

        if lst[0] == tag:
            result.append(lst)

        for i in lst[1:]:
            if isinstance(i, list):
                result.extend(self._recursive_finder(i, tag))

        return result


def main(xmlfilename, tag):
    doc = p58.StanfordDocument(xmlfilename)
    sentences = doc.sentences.findall('sentence')
    all_tag_phrases = []

    for i,sentence in enumerate(sentences):
        parser = TreeParser()
        tree_string = sentence.find('parse').text
        parser.parse(tree_string)
        all_tag_phrases.append(parser.get_phrase(tag))

    return all_tag_phrases

def str_phrase(phrase):
    output = []

    for i in phrase:
        if isinstance(i, list):
            if isinstance(i[1], list):
                output += str_phrase(i)
            else:
                output.append(i[1])

    return output

if __name__ == '__main__':
    all_np_phrases = main(sys.argv[1], 'NP')

    for np_phrases in all_np_phrases:
        for np_phrase in np_phrases:
            phrase_list = str_phrase(np_phrase)
            print(phrase_list)

    
