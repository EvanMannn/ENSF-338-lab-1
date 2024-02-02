import json
import collections.abc
import timeit
import numpy as np
import matplotlib.pyplot as plt



setupcode = '''
import json
import collections.abc
file = open('C:/ENSF_338/ENSF-338-lab-1/large-file.json', 'r', encoding='utf-8')
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
def forloop(dat, numRecords):
    i = 0
    for ary in dat:
        if i > numRecords: break
        check(ary)
        i+=1'''




times1000 = timeit.repeat(setup=setupcode, stmt='forloop(data, 1000)', repeat = 1000, number = 1)

plt.hist(times1000)
plt.title("Histogram of time taken to compute 1000 records")
plt.xlabel("Seconds to Compute")
plt.ylabel("Frequency")
plt.show()

#times2000 = timeit.repeat(setup=setupcode, stmt='forloop(data, 2000)', repeat = 100, number = 1)
#times5000 = timeit.repeat(setup=setupcode, stmt='forloop(data, 5000)', repeat = 100, number = 1)
#times10000 = timeit.repeat(setup=setupcode, stmt='forloop(data, 10000)', repeat = 100, number = 1)

#averages = []
#averages.append(sum(times1000)/len(times1000))
#averages.append(sum(times2000)/len(times2000))
#averages.append(sum(times5000)/len(times5000))
#averages.append(sum(times10000)/len(times10000))

#listlengths = [1000, 2000, 5000, 10000]
#slope, intercept = np.polyfit(listlengths, averages, 1)
#plt.scatter(listlengths, averages)
#linevalues = [slope * x + intercept for x in listlengths]
#plt.plot(listlengths, linevalues, 'r')
#plt.xlabel("number of records")
#plt.ylabel("average computation time")
#plt.title("Linear regression plot of Average computation time as a function of the number of records being searched")
#plt.show()