num=int(bin(4349)[2:])
print(num)

s=['1', '2', '3']
for x in s:
    for y in s:
        for z in s:
            print(x+y+z)


s = "012345671"
sp=list(s)
print(sp.count('1'))
print(sp.index(max(sp)))
print(sp)
print(min(sp))

a=list(map(int,sp))
print(a)

s=[]
a[-1]
b=a[::-1]
print(b)


a.sort(reverse=True)
print(a)


sp=[x for x in range(8)]
print(sp)

