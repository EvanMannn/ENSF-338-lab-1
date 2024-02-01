f = open("pg2701.txt", "r", encoding="utf-8")
f.seek(843, 0)
numVowels = []
for line in f:
    words = line.split(' ')
    for word in words:
        curVowels = 0
        curVowels += word.count('a')
        curVowels += word.count('e')
        curVowels += word.count('i')
        curVowels += word.count('o')
        curVowels += word.count('u')
        curVowels += word.count('y')
        curVowels += word.count('A')
        curVowels += word.count('E')
        curVowels += word.count('I')
        curVowels += word.count('O')
        curVowels += word.count('U')
        curVowels += word.count('Y')
        numVowels.append(curVowels)

sum = 0
for num in numVowels:
    sum += num

average = sum / len(numVowels)
print(average)