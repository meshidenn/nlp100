import re

def check_sw(swlist,line):
    check = False
    for word in swlist:
        cm = re.compile(word.strip())
        t = cm.search(line)
        if t:
            check = True
            break

    return check
        
def main():
    swlist = []
    
    with open('stopword.txt','r') as f:
        for word in f:
            swlist.append(word)

    with open('sentiment.txt','r') as infile:
        for line in infile:
            check = check_sw(swlist,line)
            print(check)

    return 'end'

if __name__ == '__main__':
    end = main()
