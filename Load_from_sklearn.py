#										FLOWER PREDICTION BASED ON IRIS FLOWER DATASET
#										     (Importing from sklearn library)
#Importing modules

#Note, here we have created pd as an alias to panda, so we wont have to write panda.abc ,we can write pd.abc
import pandas as pd
import numpy as np

#We can also write from matplotlib import pyplot as pt but we have done this to make code more compact and save time
import matplotlib.pyplot as plt

#Importing the Iris Dataset from sklearn
#We can import the dataset from other source too like:
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
#dataset = pd.read_csv(url, header=names)
#we can also put header=None 
#By importing like above, the data is split into training set(.tra) and test set(.tes)
from sklearn import datasets
iris = datasets.load_iris()

#Printing the keys
print("These are the keys in the iris dataset:--> %s" % (iris.keys()))

#Printing the description
usinput=input("Do you want to see the description of the Iris dataset(y/n)?:")
if usinput == 'y':
	print(iris.DESCR)

#Isolating the data
iris_data=iris.data
usinput=input("Do you want to see the data(y/n)?:")
if usinput == 'y':
	print(iris.feature_names)
	print(iris_data)

#Data shape
usinput=input("Do you want to see the data shape(y/n)?:")
if usinput == 'y':
	print(iris_data.shape)

#Setting figure size(The size of our graph) for matplotlib, it is in (width,height) and inches
fig=plt.figure(figsize=(5,5))
# Adjusting the subplots 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
# For each of the 64 images
for i in range(4):
    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    # Display an image at the i-th position
    #ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    # label the image with the target value
    ax.text(0, 7, str(iris.target[i]))
#Now to show the plot
plt.show()
#Command to use to print all the attributes of an object-->print(dir(object))
