from stemming.porter2 import stem
import nltk

def stemming(file):
    stems = []
    porter = nltk.PorterStemmer()
    for word in file:
        result = stem(word.strip())
        print(word.strip(),result.strip())
        stems.append(result.strip())

    return(stems)

def main():
    with open('nlp_words.txt','r') as file:
        stems = stemming(file)

    return(stems)

if __name__ == '__main__':
    stems = main()
    for i,stem in enumerate(stems):
        if i == 0:
            with open('nlp_stems.txt','w') as f:
                print(stem,file=f)
        else:
            with open('nlp_stems.txt','a') as f:
                print(stem,file=f)
