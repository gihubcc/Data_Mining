import jieba
import jieba.posseg as pseg
from sklearn.feature_extraction.text import CountVectorizer


f=open('stopword.txt')
stopw=[]
while 1:
        line =f.readline()
        if not line:
                break
        stopw[line]=1;
f.close()

if stopw.has_key("1"):
        print("haha ")



f=open('a.train')

label1=[]
label2=[]
label3=[]
tex=[]
i=30

jieba.load_userdict("sougou.dic")

while i:
        line =f.readline()
        if not line:
                break

        words=jieba.cut(line[39:])
        tem=""
        for seg in words :
                tem=tem+" "+seg

        tex.append(tem)
        a=line.split()
        label1.append(a[1])
        label2.append(a[2])
        label3.append(a[3])
        i=i-1
f.close()


f=open('a.test')
i=30
while i:
        line =f.readline()
        if not line:
                break
        words=jieba.cut(line[33:])
        tem=""
        for seg in words :
                tem=tem+" "+seg
        tex.append(tem)
        i=i-1

print(tex)

f = open("seg.txt", "w+")
f.write(' '.join(tex))
f.close()


f = open("lable1.txt", "w+")
f.write('\n'.join(label1))
f.close()

f = open("lable2.txt", "w+")
f.write('\n'.join(label2))
f.close()

f = open("lable3.txt", "w+")
f.write('\n'.join(label3))
f.close()


#for seg in words :
#        print(seg.word)
#print(seg.flag)