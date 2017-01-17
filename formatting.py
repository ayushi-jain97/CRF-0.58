f=open("formatted.txt","r")
f1=open("test.txt","a")
f2=open("train.txt","a")
lines=f.readlines()
for line in lines[0:3000]:
	l=line.strip().split()
	f2.write(l[0]+' '+l[1]+' '+l[2]+' '+l[3]+'\n')
for line in lines[3000:4000]:
	l=line.strip().split()
	f1.write(l[0]+' '+l[1]+' '+l[2]+' '+l[3]+'\n')
f.close()
f2.close()
f1.close()
