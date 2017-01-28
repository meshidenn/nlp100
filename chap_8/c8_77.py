import c8_73 as p73
from sklearn.linear_model import LogisticRegression

def pre_and_re(y,pre):
    n = len([a for a in y if a == 1])
    m = len([b for b in y if b == -1])
    o = len([c for c in pre if c == 1])
    p = len([d for d in pre if d == -1])
            
    a = len([i for i,j in zip(y,pre) if i == j and i == 1])
    b = len([i for i,j in zip(y,pre) if i != j and i == 1])
    c = len([i for i,j in zip(y,pre) if i != j and i != -1])
    d = len([i for i,j in zip(y,pre) if i == j and i == -1])

    precision = a/o
    recall = a/n
    f1 = (2*precision*recall)/(precision + recall)

    return precision,recall,f1
       

def main():
    swlist = []
    with open('stopword.txt','r') as sw:
        for line in sw:
            swlist.append(line.strip())
    print(swlist)
       
    with open('pn_en.dic','r') as f:
        wpdict = p73.mkwpdict(swlist,f)

    with open('sentiment.txt','r') as sent:
        x,y,slist = p73.makexy(wpdict,sent)

    model = p73.learning(x,y)

    pre = model.predict(x)
    prob = model.predict_proba(x)
    coef = model.coef_

    precision,recall,f1 = pre_and_re(y,pre)
    return precision,recall,f1

if __name__ == '__main__':
    precision,recall,f1 = main()
    print(precision,recall,f1)
