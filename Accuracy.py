import sklearn.metrics as metrics
from pandas_ml import ConfusionMatrix
f=open('output.txt','r')

lines=f.readlines()
y_true=[]
y_pred=[]
for line in lines:
	l=line.strip().split('\t')
	if(len(l)>4):
		y_true.append(l[3])
		y_pred.append(l[4])

print metrics.accuracy_score(y_true,y_pred)
print metrics.recall_score(y_true,y_pred,average='micro')
print metrics.precision_score(y_true,y_pred,average='micro')
print metrics.f1_score(y_true,y_pred,average='micro')
cm=ConfusionMatrix(y_true,y_pred)
cm.print_stats()
