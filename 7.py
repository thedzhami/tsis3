print(len(set(input().split()) & set(input().split())))


print(len(set(set(input().split())^set(input().split()))))
