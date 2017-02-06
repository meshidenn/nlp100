import re
import nltk

def tokenizer(raw):
    sentences = []
    tokens = []

    for line in raw:
        raw_tokens = line.split()
        for token in raw_tokens:
            token1 = token.strip('.')
            token2 = token1.strip(',')
            token3 = token2.strip('!')
            token4 = token3.strip('?')
            token5 = token4.strip(':')
            token6 = token5.strip(';')
            token7 = token6.strip('(')
            token8 = token7.strip(')')
            token9 = token8.strip('[')
            token10 = token9.strip(']')
            token11 = token10.strip('\'')
            token12 = token11.strip('\"')
            if len(token12) != 0:
                tokens.append(token12)
#                print(token12)

    return tokens
        

def main():
    with open('enwiki-20150112-400-r10-105752.txt','r') as f:
        tokens = tokenizer(f)

    return tokens

if __name__  == '__main__':
    tokens = main()
    print(tokens)
    out = ''

    with open('proc.txt','w') as f:
        for token in tokens:
            out += token + ' '

        print(out,file=f)


        
