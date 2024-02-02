import json
import collections.abc
import timeit



setupcode = '''
import json
import collections.abc
file = open('large-file.json', 'r', encoding='utf-8')
data = json.load(file)
def check(dictionary):
    global counter
    for record in dictionary.keys():
        if record == "size":
            dictionary["size"] = 35
        elif isinstance(dictionary[record], dict):
            check(dictionary[record])
        elif isinstance(dictionary[record], collections.abc.Sequence):
            for item in dictionary[record]:
                if isinstance(item, dict):
                    check(item)
def forloop(dat):
    for ary in dat:
        check(ary)'''




time = timeit.repeat(setup=setupcode, stmt='forloop(data)', repeat = 10, number = 1)
print(time)
total = 0
for x in time:
    total += x
print("average execution time is", total/10)
#for record in data:
#   record["size"] = 35
#   if isinstance(record, dict):

#for ary in data:
#    check(ary)
file = open('large-file.json', 'r', encoding='utf-8')
data = json.load(file)


output_data = data[::-1]
with open("output.2.3.json", "w") as output_file:
    json.dump(output_data, output_file, indent=2)

