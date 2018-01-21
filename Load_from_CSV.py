#										FLOWER PREDICTION BASED ON IRIS FLOWER DATASET
#										     (Importing from CSV file)
#Importing the modules

#Creating an alias
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt

from pd.tools.plotting import scatter_matrix
from sk import model_selection
from sk.metrics import classification_report, confusion_matrix, accuracy_score
from sk.linear_model import LogisticRegression
from sk.tree import DecisionTreeClassifier
from sk.neighbors import KNeighborsClassifier
from sk.discriminant_analysis import LinearDiscriminantAnalysis
from sk.naive_bayes import GaussianNB
from sk.svm import SVC

# Loading the dataset
#Provide a url from which to take the CSV file
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

#Store the name of the attributes in form of list
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

#Using the read_csv function from pandas to read the CSV file  
dataset = pd.read_csv(url, names=names)
# head
print(dataset.head(20))