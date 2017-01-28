import c8_73 as p73
import c8_77 as p77
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt


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

    model = p73.learning(x,y)
    ppap = model.predict_proba(x)
    pp = ppap[:,1]

    precision, recall, thresholds = precision_recall_curve(y,pp)

#    for p,r,t in zip(precision, recall, thresholds):
#        print(p,r,t)
    ave = average_precision_score(y,pp)

    return precision,recall,thresholds,ave
    


if __name__ == '__main__':
    pre,re,th,ave = main()
    lw = 2

    plt.clf()
    plt.plot(re,pre, lw = lw, color = 'navy', label='Precision-Recall curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0,1.05])
    plt.xlim([0.0,1.0])
    plt.title('Precision-Recall example:AUC={0:0.2f} '.format(ave))
    plt.legend(loc="lower left")
    plt.show()


    
