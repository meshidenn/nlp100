# -*- coding utf-8 -*-

import sys
import pickle
import scipy as sp
import numpy as np
import scipy.spatial.distance as distance
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


def main(nmv_file):
    with open(nmv_file,'rb') as wr:
        nvms = pickle.load(wr)

        nvms_list = []
    for k in nvms:
        tmp = nvms[k].tolist()
        nvms_list.append(tmp)

    cust_array = np.array(nvms_list)
    cast_array = cust_array.T

    model = TSNE()
    X = model.fit_transform(cast_array)
    plt.figure(2,figsize=(8,6))
    plt.clf()
    plt.plot(X[:,0], X[:,1], ".")
    plt.show()
    

if __name__ == '__main__':
    nmv_file = sys.argv[1]
    main(nmv_file)

