#removes duplicates from [3,1,2,3,2,4]

seen = set()
out = []
for x in [3,1,2,3,2,4]:
    if x not in seen:
        seen.add(x)
        out.append(x)

    print(x)
