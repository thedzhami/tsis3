a=[]
min=100
for i in input().split():
    a.append( int(i))
    k=int(input())
if (k>0):
    for i in range(k-1, len(a)):
        a.insert(0, a.pop(-1))
else:
    for i in range(abs(k)):
        a.append(a.pop(0))
print(' '.join(str(i) for i in a))
