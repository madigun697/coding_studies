print("""
import db_conn
import pandas as pd
import numpy as np
import copy
import collections
import statsmodels.formula.api as sm
import scipy.stats as st
import matplotlib.pyplot  as plt
from IPython.display import display
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import seaborn as sns

plt.style.use('dark_background')

plt.rcParams["figure.figsize"] = (20,10)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.color'] = 'r'
plt.rcParams['axes.grid'] = True 

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
""")