import timeit
#CHAPTER 1. LOOMING.    This line assumed to be line 843 in the txt file, not line 41 as they are the exact same
testcode = '''
def countVowels():
    numCons = []
    for line in lines[842:]:
        words = line.split(' ')
        for word in words:
            temp = 0
            for letter in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
                temp += word.count(letter)
            numCons.append(temp)

    sum = 0
    for num in numCons:
        sum += num

    average = sum / len(numCons)
    return average
'''

f = open("pg2701.txt", "r", encoding="utf-8")
lines = f.readlines()
times = timeit.repeat(stmt=testcode, repeat=100)
sum = 0
for time in times:
    sum += time
average = sum / len(times)

print(f'The average time to count the number of vowels per word starting from line 843 "CHAPTER 1. LOOMING.", is {average}')

#print(f'The average number of vowels per word starting from line 843 "CHAPTER 1. LOOMING.", is {average}')