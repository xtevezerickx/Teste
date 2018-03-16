
# coding: utf-8

# In[21]:

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import graphviz 
from sklearn import preprocessing
from sklearn import tree


# In[32]:

dataSet = pd.read_csv('dog.csv', delimiter=',')
lb_make = preprocessing.LabelEncoder()


# In[33]:

dataSet.head()


# In[34]:

decisionTree = DecisionTreeClassifier(criterion="entropy")


# In[35]:

dataSet['Nome'] = dataSet.Nome.astype(str)
dataSet['Idade'] = dataSet.Idade.str.replace(',','.').astype(float)
dataSet['Cor'] = dataSet.Cor.astype(str)
dataSet['Cor'] = lb_make.fit_transform(dataSet["Cor"])
dataSet['Raça'] = dataSet.Raça.astype(str)
dataSet['Raça'] = lb_make.fit_transform(dataSet["Raça"])
dataSet['Porte'] = dataSet.Porte.astype(str)
dataSet['Porte'] = lb_make.fit_transform(dataSet["Porte"])


# In[36]:

x_treino = dataSet.values[:,1:4]
y_treino = dataSet.values[:,5]
dataSet.dtypes


# In[37]:

modelo = decisionTree.fit(x_treino, list(y_treino))


# In[38]:

dotData = tree.export_graphviz(modelo, out_file=None)
graph = graphviz.Source(dotData)
graph.render("iris")
print(list(dataSet['Clazz']))


# In[39]:

dot_data = tree.export_graphviz(decisionTree, out_file=None, 
                         feature_names=list(dataSet),  
                         class_names=['1','0'],  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 


# In[ ]:



