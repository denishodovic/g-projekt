fname = raw_input("Enter file name: ")
#counter = 0
fh = open(fname)


di = dict()

for line in fh:
    line = line.rstrip()

    if not line.startswith('From '):
        continue
    words = line.split()

    # print(words[1])
    #counter = counter + 1

    p = words[1]
    print(p)
    di[p] = di.get(p, 0)+1
print(di)

largest = -1
name = None
for k, v in di.items():
    if v > largest:
        largest = v
        name = k
print(name, largest)
