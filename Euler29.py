myset = {}
myset = set(myset)
for a in range(2,101):
    for b in range(2,101):
        myset.add(a**b)

myset = list(myset)

print(sorted(myset))
print(len(myset))