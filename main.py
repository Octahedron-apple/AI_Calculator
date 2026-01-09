Tokenfrom sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
xt=[]
yt=[]
xte=[]
yte=[]
d=0
with open("dat.txt","r") as f:
    a=f.readlines()
for i in a:
    xt.append(i.split("=")[0])
    yt.append(i.split("=")[1])
with open("test.txt","r") as f:
    a=f.readlines()
for i in a:
    xte.append(i.split("=")[0])
    yte.append(i.split("=")[1])
