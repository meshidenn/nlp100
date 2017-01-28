
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．
"""

import sys
import n56


class TreeParser():

    def __init__(self):
        self.root = None
        self._stack = [[]]

    def parse(self, tree_string):
        reading = []
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
            else:  # string
                reading.append(character)

            print('in',self._stack)
        
        self.root = self._stack.pop() #default [] is top, so pop return result 

        print('pop',self.root)

    def get_phrase(self, tag):
        s = self.root[0][1] # extract under Root
        return self._recursive_finder(s, tag)

    def _recursive_finder(self, lst, tag):
        result = []

        if lst[0] == tag: # for list only np
            result.append(lst)

        for i in lst[1:]:
            if isinstance(i, list):
                result.extend(self._recursive_finder(i, tag))

        return result


def main(xmlfilename, tag):
    doc = n56.StanfordDocument(xmlfilename)
    sentences = doc.sentences.findall('sentence')
    all_tag_phrases = []

    for sentence in sentences:
        parser = TreeParser()
        tree_string = sentence.find('parse').text
        parser.parse(tree_string)
        print('root',parser.root)
        print('stack',parser._stack)
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
#    print('\n\n\n',all_np_phrases)

    for np_phrases in all_np_phrases:
        for np_phrase in np_phrases:
            phrase_list = str_phrase(np_phrase)
            np_string = n56.sentence_prettify(phrase_list)
            print(phrase_list)
