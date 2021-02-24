a=[]
min=100
for i in input().split():
    a.append( int(i))
for i in range(len(a)):
    if a[i] == 0:
        a.append(a.pop(i))
print(a)
