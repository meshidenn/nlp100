# -*- coding utf-8 -*-

import sys
import pickle
from sklearn.cluster import KMeans
import numpy as np

def main(nmv_file):
    with open(nmv_file,'rb') as wr:
       nvms = pickle.load(wr)

    nvms_list = []
    for k in nvms:
        tmp = nvms[k].tolist()
        nvms_list.append(tmp)

    cust_array = np.array(nvms_list)
    cast_array = cust_array.T

    pred = KMeans(n_clusters = 5).fit_predict(cust_array)
    print(pred)


if __name__ == '__main__':
    nmv_file = sys.argv[1]
    main(nmv_file)

