import jieba
import jieba.posseg as pseg
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfTransformer

f=open("seg.txt")

corpus=[];

linenum=0

while 1:
        line =f.readline()
        if not line:
                break
        corpus.append(line)
        linenum=linenum+1
f.close()

vectorizer = CountVectorizer()
tf = vectorizer.fit_transform(corpus)

word = vectorizer.get_feature_names()

print(len(word))

tf_array=tf.toarray()

s=sum(tf_array)


i=len(word)-1
while i>=0:
    if (s[i]<2):
        del word[i]
    i=i-1
print(len(word))

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(tf)

a=sum(tfidf)


#print(a)

print("aaa")
print(a.toarray()[0][0])
'''
f = open("tfidf.txt", "w+")

print(linenum)

for i in range(linenum):
    print(i)
    for j in range(len(word)):
        f.write(str(weight[0][j])+" ");
    f.write("\n")

f.close()
'''