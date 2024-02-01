import sys

#The code was printing yes for every single number that wasn't a factor of number, changing the indent fixed the issue
#Also the print statements were updated to make it more clear what the code was doing.

def do_stuff():
    number = int(sys.argv[1])
    if number < 2:
        print('No')
    else:
        for i in range(2, number):
            if number % i == 0:
                print(f'No {number} is not a prime')
                return
        print(f'Yes {number} is a prime')

# Test the function
do_stuff()
