import c4_30_2 as p30
import matplotlib.pyplot as plt

def read(file):
    out = []
    buf = []
    for line in file:
        word, cnt = line.split(",")
        cou = cnt.rstrip('\n')
        buf.append(word)
        buf.append(cou)
        out.append(buf)
        buf = []

    return out
     

def main():
    with open('neko.txt.freq','r') as file:
        freq = read(file)

    top10 = []
    for i in range(10):
        top10.append(freq[i])
    
    return top10

if __name__ == '__main__':
    top10 = main()
    x = []
    y = []
    print(top10)
    for i in range(10):
        x.append(top10[i][0])
        y.append(int(top10[i][1]))
        
    print(x,y)
#    fig = plt.figure()
#    print("type(fig): {}".format(type(fig)))
#    ax = fig.add_subplot(1,1,1)

#    ax.set_xlabel("word")
#    ax.set_ylabel("freq")
#    ax.set_title("word_freq")

    plt.barh(range(0,10),y)
    plt.yticks(range(0,10),x)
    plt.xlabel("freq")
    plt.ylabel("word")
    plt.title("word_freq")
    plt.show()

    
