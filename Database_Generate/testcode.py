
a = [1,4,1,'4',1,4,1,4,4,335]

b = [x+1 for x in a]
c = [x-2 for x in b]


d = [a,b,c]
print(d)
d = sorted(d)
print(d)
d = map(list, zip(*d))
print(d)
