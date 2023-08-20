
import numpy as np 
import pandas as pd 
import os
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import math
import json
import time
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
import joblib
import scipy.sparse
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
import warnings; warnings.simplefilter('ignore')
import sys


from sklearn.decomposition import TruncatedSVD



def train(x):
    data=pd.read_csv("flipkart_grid/data_and_clean/final_merged.csv")
    data.drop(['time'], axis=1,inplace=True)
    data.columns=['productId','userId','Rating']
    no_of_rated_products_per_user = data.groupby(by='userId')['Rating'].count().sort_values(ascending=False)
    new_df=data.groupby("productId").filter(lambda x:x['Rating'].count() >=50)
    ratings_mean_count = pd.DataFrame(new_df.groupby('productId')['Rating'].mean())
    ratings_mean_count['rating_counts'] = pd.DataFrame(new_df.groupby('productId')['Rating'].count())

    new_df1=new_df.head(100000)
    ratings_matrix = new_df1.pivot_table(values='Rating', index='userId', columns='productId', fill_value=0)
    X = ratings_matrix.T

    X1 = X
    SVD = TruncatedSVD(n_components=10)
    decomposed_matrix = SVD.fit_transform(X)
    decomposed_matrix.shape
    correlation_matrix = np.corrcoef(decomposed_matrix)
    #"B000050FDT"
    i = x

    product_names = list(X.index)
    product_ID = product_names.index(i)

    correlation_product_ID = correlation_matrix[product_ID]
    Recommend = list(X.index[correlation_product_ID > 0.65])

    # Removes the item already bought by the customer
    Recommend.remove(i) 

    print('\n'.join(Recommend[0:15]))
if __name__=="__main__":
    x=sys.argv[1]
    train(x)

