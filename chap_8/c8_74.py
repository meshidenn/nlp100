import c8_73 as p73
from sklearn.linear_model import LogisticRegression

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
        
    return y,pre,prob,coef,slist

if __name__ == '__main__':
    y,pre,prob,coef,slist = main()
    pair = []
    for i,j,k in zip(y,pre,prob):
        print(i,j,k)
    for co in coef:
        for w,c in zip(slist,co):
            pair.append((w,c))

    desc = sorted(pair,key=lambda x:x[1],reverse=True)
    asc = sorted(pair,key=lambda x:x[1])

    for i in range(10):
        print(desc[i])
    for i in range(10):
        print(asc[i])

