# -*- coding: utf-8 -*-

import sys
import pickle
import scipy as sp
import numpy as np
import scipy.spatial.distance as distance
from matplotlib.pyplot import show
from scipy.cluster.hierarchy import linkage, dendrogram


def main(nmv_file):
    with open(nmv_file,'rb') as wr:
        nvms = pickle.load(wr)

        nvms_list = []
    for k in nvms:
        tmp = nvms[k].tolist()
        nvms_list.append(tmp)

    cust_array = np.array(nvms_list)
    cast_array = cust_array.T

    result1 = linkage(cast_array, method = 'ward')
    dendrogram(result1)
    show()

if __name__ == '__main__':
    nmv_file = sys.argv[1]
    main(nmv_file)

               


