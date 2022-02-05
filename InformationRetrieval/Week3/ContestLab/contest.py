import requests

dictionary = ['caterpillar',
              'alligator',
              'crocodile',
              'groundhog',
              'elephant',
              'cheetah',
              'butterfly',
              'anaconda',
              'wolverine',
              'wolf',
              'firefox',
              'badger',
              'buffalo',
              'cassowary',
              'chinchilla',
              'chimpanzee',
              'flamingo',
              'grasshopper',
              'hummingbird',
              'penguin',
              'bluebird']


def levenstein(str1, str2):
    # Creating an array
    m = len(str1)
    n = len(str2)
    dp = [range(n+1)][range(m+1)]
    

def levenstein(str1, str2):
    # Creating an array
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return(dp[m][n])

def wildcard(data, word):
    wp = 0
    dp = 0
    buff = ''
    while wp != len(data) 
    

with open('input.txt', 'r') as f:
    action, data = f.read().split('\n')
    if 'typo' == action:
        res = sorted(list(map(lambda w: (w, levenstein(w, data)), dictionary)), key = lambda x: x[1])[0][0]
    elif 'wildcard' == action:
        print('aboba')

with open('output.txt', 'w+') as out:
    out.write(res)