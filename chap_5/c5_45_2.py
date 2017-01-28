import c5_41_2 as p41

def exreact_verbcase_pat(sentence):
    verbcase_pat = []

    for chunk in sentence:
        if chunk.include_pos('動詞'):
            print('a_',chunk.srcs)
            src_chunks = [sentence[src] for src in chunk.srcs]
            print(src_chunks)
            src_chunks_case = list(filter(lambda src_chunk: src_chunk.morphs_of_pos1('格助詞'), src_chunks))
            if src_chunks_case:
                verbcase_pat.append((chunk, src_chunks_case))

    return verbcase_pat

def main():
    sentences = p41.main()
    verbcase_pats = []

    for sentence in sentences:
        verbcase_pats.append(exreact_verbcase_pat(sentence))

    return verbcase_pats

if __name__ == '__main__':
    verbcase_pats = main()
    for verbcase_pat in verbcase_pats:
        for verb, src_chunk in verbcase_pat:
            col1 = verb.morphs_of_pos('動詞')[-1].base
            cases = [src_chunk.morphs_of_pos1('格助詞')[-1].base for src_chunk in src_chunks]
            col2 = "".join(sorted(cases))
            print(col1,col2, sep="\t")
