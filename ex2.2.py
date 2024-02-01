#CHAPTER 1. LOOMING.    This line assumed to be line 843 in the txt file, not line 41 as they are the exact same

f = open("pg2701.txt", "r", encoding="utf-8")
lines = f.readlines()
numCons = []
for line in lines[842:]:
    words = line.split(' ')
    for word in words:
        temp = 0
        for letter in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', 'B', 'C', 'D', 'F', 'G','H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']:
            temp += word.count(letter)
        numCons.append(temp)

sum = 0
for num in numCons:
    sum += num

average = sum / len(numCons)
print(f'The average number of consonants per word starting from line 843 "CHAPTER 1. LOOMING.", is {average}')