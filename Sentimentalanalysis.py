from textblob import TextBlob
import csv
file=open('pro.csv', 'w', newline='')
fi=open('review.csv', 'r', newline='')
writer = csv.writer(file)
cs = csv.reader(fi)
cs2=csv.reader(file)
l=list()
for i in cs:
    
    l+=[TextBlob(i[1]).sentiment.polarity,]
print(l)

lr=list()
for i in l:
    if i>0:
        lr+=["Positive",]
    elif i<0:
        lr+=["Negetive",]
    else:
        lr+=["Moderate",]
print(lr)
writer.writerows(lr)