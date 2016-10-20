import jieba
import jieba.posseg as pseg
from sklearn.feature_extraction.text import CountVectorizer

f=open('a.train',encoding='utf-8')
i=0;
label1=[];
label2=[];
label3=[];
tex=[];

i=10;

while i:
        line =f.readline()
        if not line:
                break

        words=jieba.cut(line[39:])
        tem="";
        for seg in words :
                tem=tem+" "+seg;

        tex.append(tem);
        a=line.split();
        label1.append(a[1]);
        label2.append(a[2]);
        label3.append(a[3]);
        i=i-1

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(tex)
word = vectorizer.get_feature_names()

print("**********************")
print(X.toarray())
print(len(word))


#for seg in words :
#        print(seg.word)
#print(seg.flag)