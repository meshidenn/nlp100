import numpy as np
import scipy as sp
import sklearn as sk
from scipy import io, sparse
from sklearn.decomposition import PCA, TruncatedSVD


matrix = io.loadmat("ppmi_matrix")["ppmi"]
pca = TruncatedSVD(300)
decom_matrix = pca.fit_transform(matrix)
io.savemat("pca_result",{"pca_300":decom_matrix})
