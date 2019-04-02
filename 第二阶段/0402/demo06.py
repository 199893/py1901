L=[x*x for x in range(5)]
print(L,type(L))

G=(x*x for x in range(5))
print(G,type(G))

print(next(G))

for i in G:
    print(i)


