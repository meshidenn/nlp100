

def word(file):
    words = []
    for line in file:
        proc_word = []
        word = line.split()
        for w in word:
            w.strip()
            proc_word.append(w)
        words.append(proc_word)
        words.append(' ')
    return(words)
    
def main():
    with open('nlp_sentence.txt','r') as file:
        words = word(file)

    return words

if __name__ ==  '__main__':
    words = main()
    for i,word in enumerate(words):
        print(word)
        for j,w in enumerate(word):
            if i == 0 and j == 0:
                with open('nlp_words.txt','w') as out:
                    print(w,file=out)
            else:
                with open('nlp_words.txt','a') as out:
                    print(w,file=out)
