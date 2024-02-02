import json
import matplotlib.pyplot as plt
import numpy as np

def seperateData(d):
    
    for item in d:
        if item["loudness"] >= -8:
            highLoudness.append(item)
        else:
            lowLoudness.append(item) 



lowLoudness = []
highLoudness = []


f = open("songdata.json", "r", encoding="utf-8")
data = json.load(f)
seperateData(data)

lowLoudTempos = [x["tempo"] for x in lowLoudness]
highLoudTempos = [x["tempo"] for x in highLoudness]

plt.hist(lowLoudTempos, bins=25, linewidth=0.5, edgecolor="white")
plt.ylabel("Counts")
plt.xlabel("Tempo Ranges")
plt.title("Tempo Histogram for songs with a loudness less than -8")
plt.show()

plt.hist(highLoudTempos, bins=25, linewidth=0.5, edgecolor="white")
plt.ylabel("Counts")
plt.xlabel("Tempo Ranges")
plt.title("Tempo Histogram for songs with a loudness greater than or equal to -8")
plt.show()