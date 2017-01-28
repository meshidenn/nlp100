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

    return freq

if __name__ == '__main__':
    freq = main()
    n = len(freq)
    x = []
    y = []
    for i in range(n):
        x.append(i)
        y.append(int(freq[i][1]))
        
#    print(x,y)
#    fig = plt.figure()
#    print("type(fig): {}".format(type(fig)))
#    ax = fig.add_subplot(1,1,1)

#    ax.set_xlabel("word")
#    ax.set_ylabel("freq")
#    ax.set_title("word_freq")

    plt.xscale("log")
    plt.yscale("log")
    plt.plot(x,y)
    plt.xlabel("rank")
    plt.ylabel("freq")
    plt.title("Zipf")
    plt.show()
