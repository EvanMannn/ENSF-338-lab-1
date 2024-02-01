import json
f = open("large-file.json", encoding="utf-8")
data = json.load(f)
for i in data:
    print(i)