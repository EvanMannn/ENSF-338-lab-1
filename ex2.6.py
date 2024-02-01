import timeit

def fact(n):
    nf = 1
    for n in range(1, n+1):
        nf = nf * n
    print(nf)

setupcode = '''
def fact(n):
    nf = 1
    for n in range(1, n+1):
        nf = nf * n
    return nf
'''
forsetupcode = '''
def fact(n):
    nf = 1
    for n in range(1, n+1):
        nf = nf * n
    return nf
def factfor():
    for n in range(1,101):
        fact(n)
'''
listsetupcode = '''
def fact(n):
    nf = 1
    for n in range(1, n+1):
        nf = nf * n
    return nf
def factlist():
    list = [fact(n) for n in range(1,101)]
'''

time = timeit.repeat(setup=setupcode, stmt='fact(100)', repeat=1, number=10000)
print("\n")
print(time)


ltime = timeit.repeat(setup=listsetupcode, stmt='factlist()',repeat=1, number=1000)
print("\n")
print(ltime)



ftime = timeit.repeat(setup=forsetupcode, stmt='factfor()',repeat=1, number=1000)
print("\n")
print(ftime)