# From users = [{"id":1,"age":30},{"id":2,"age":25},{"id":3,"age":30}], build {30:[1,3], 25:[2]}.

from collections import defaultdict

users = [{"id": 1, "age": 30},
         {"id": 2, "age": 25},
         {"id": 3, "age": 30}]

groups = defaultdict(list)
for u in users:
    groups[u["age"]].append(u["id"])

result = dict(groups)
print(result)

