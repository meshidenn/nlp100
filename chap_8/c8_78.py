import c8_73 as p73
import c8_77 as p77
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold

def main():
    swlist = []
    with open('stopword.txt','r') as sw:
        for line in sw:
            swlist.append(line.strip())
        
    with open('pn_en.dic','r') as f:
        wpdict = p73.mkwpdict(swlist,f)

    with open('sentiment.txt','r') as sent:
        x,y,slist = p73.makexy(wpdict,sent)

    ss = StratifiedKFold(n_splits=5,shuffle=True)

    i = 0
    for train_index, test_index in ss.split(x,y):
        i += 1
        x_train = [x[j] for j in train_index]
        x_test = [x[j] for j in test_index]
        y_train = [y[j] for j in train_index]
        y_test = [y[j] for j in test_index]
        
        model = p73.learning(x_train,y_train)

        score = model.score(x_test,y_test)
        pre = model.predict(x_test)
        precision,recall,f1 = p77.pre_and_re(y_test,pre)
        print(i,score,precision,recall,f1)

if __name__ == '__main__':
    main()
