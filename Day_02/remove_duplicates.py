# removes duplicates from [3,1,2,3,2,4,5,5]

seen = set()
out = []
for x in [3,1,2,3,2,4,5,5]:
    if x not in seen:
        seen.add(x) # seen is a set used to remember items we’ve already encountered (fast membership checks)
        out.append(x) # out collects the first time we see each item, preserving the original order.

print(out)
