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
text_model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])
text_model.fit(xt,yt)
with open("out.txt","w") as f:
    for i in range(len(a)):
        c=text_model.predict([xte[i]])[0]
        f.write(f"\n{i+1} Prediction :\n{xte[i]}={c}correct? {yte[i]==c}")
        d+=yte[i]==c
print("Number of correct guesses; ",d)
print("Total number of guesses:", len(a))
print("Percentage of correct sol: ", d/len(a)*100,"%")
