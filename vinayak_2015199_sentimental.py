# -*- coding: utf-8 -*-
"""Vinayak_2015199_sentimental.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13ugR3NVFBjlKPpMilqFSJ0YGoCSwKvK9
"""

from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

df = pd.read_csv('./Tweets1.csv')

df.drop(['Unnamed: 0'],axis=1,inplace=True)

df.head()

def cleanTxt(text):
 text = re.sub(r'@[A-Za-z0–9]+', '', text) #Removing @mentions
 text = re.sub(r'#', '', text) # Removing '#' hash tag
 text = re.sub(r'RT[\s]+', '', text) # Removing RT
 text = re.sub(r'https?:\/\/\S+', '', text) # Removing hyperlink
 return text

df['Tweets'] = df['Tweets'].apply(cleanTxt)
df

def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
   return  TextBlob(text).sentiment.polarity

df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
df['Polarity'] = df['Tweets'].apply(getPolarity)

df

def getAnalysis(score):
  if score < 0:
    return "Negative"
  elif score == 0:
    return "Neutral"
  else :
    return "Positive"
df['Analysis']=df['Polarity'].apply(getAnalysis)
df

# Printing the positive tweets 
print('Printing positive tweets:\n')
j=1
sortedDF = df.sort_values(by=['Polarity']) #Sort the tweets
for i in range(0, sortedDF.shape[0] ):
  if( sortedDF['Analysis'][i] == 'Positive'):
    print(str(j) + ') '+ sortedDF['Tweets'][i])
    print()
    j= j+1

# Printing the negative tweets  
print('Printing negative tweets:\n')
j=1
sortedDF = df.sort_values(by=['Polarity'],ascending=False) #Sort the tweets
for i in range(0, sortedDF.shape[0] ):
  if( sortedDF['Analysis'][i] == 'Negative'):
    print(str(j) + ') '+sortedDF['Tweets'][i])
    print()
    j=j+1

# Plotting the graph
plt.figure(figsize=(8,6)) 
for i in range(0, df.shape[0]):
  plt.scatter(df["Subjectivity"][i],df["Polarity"][i]) 
# plt.scatter(x,y,color)
plt.title('Sentiment Analysis') 
plt.ylabel('Polarity') 
plt.xlabel('Subjectivity') 
plt.show()

# Printing the percentage of positive tweets
ptweets = df[df.Analysis == 'Positive']
ptweets = ptweets['Tweets']
ptweets

round( (ptweets.shape[0] / df.shape[0]) * 100 , 1)

# Printing the percentage of negative tweets
ntweets = df[df.Analysis == 'Negative']
ntweets = ntweets['Tweets']
ntweets

round( (ntweets.shape[0] / df.shape[0]) * 100, 1)

# Printing the percentage of neutral tweets
ptweets = df[df.Analysis == 'Neutral']
ptweets = ptweets['Tweets']
ptweets

round( (ptweets.shape[0] / df.shape[0]) * 100 , 1)

# displayingthe value counts
df['Analysis'].value_counts()

# Plotting and visualizing the counts
plt.figure(figsize=(10,7))
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df['Analysis'].value_counts().plot(kind = 'bar')
plt.show()