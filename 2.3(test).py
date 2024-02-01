import json
import collections.abc

counter = 0
def check(dictionary):
    global counter
    for record in dictionary.keys():
        if record == "size":
            dictionary["size"] = 35
            counter += 1
        elif isinstance(dictionary[record], dict):
            check(dictionary[record])
        elif isinstance(dictionary[record], collections.abc.Sequence):
            for item in dictionary[record]:
                if isinstance(item, dict):
                    check(item)

file =  open('large-file.json', 'r', encoding='utf-8')
data = json.load(file)


#for record in data:
#   record["size"] = 35
#   if isinstance(record, dict):

for ary in data:
    check(ary)

print(counter)
print("number missing is", 7406 - counter)

output_data = data[::-1]
with open("output.2.3.json", "w") as output_file:
    json.dump(output_data, output_file, indent=2)

