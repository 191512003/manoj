l = []
_ = input()
for i, j in enumerate(map(int,raw_input().split(" "))):
    if j == i:
        l.append(i)
if len(l) > 0:
    print " ".join(map(str,l))
else:
    print -1
