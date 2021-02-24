a=[]
min=100
for i in input().split():
    a.append( int(i))
for i in range(len(a)):
        if (a[i]<min and a[i]>0):
            min=a[i]
print(min)