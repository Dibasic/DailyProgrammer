# [2018-08-20] Challenge #366 [Easy] Word funnel 1
# https://www.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/

CHALLENGE_INPUT = { 'leave'   : 'eave'   
                  , 'reset'   : 'rest'   
                  , 'dragoon' : 'dragon' 
                  , 'eave'    : 'leave'  
                  , 'sleet'   : 'lets'   
                  , 'skiff'   : 'ski'
                  }

BONUS1_INPUT = [ 'dragoon', 'boats', 'affidavit' ]

BONUS2_INPUT = 5

# Funnel algorithm for challenge
def funnel(a: str, b: str) -> bool:
    if len(a) != len(b) + 1:
        return False
    return b in get_slices(a)

# Return all strings that are missing one letter
def get_slices(word: str) -> list:
    return [ word[:i] + word[i+1:] for i, c in enumerate(word) ]

# Return all unique slices
def get_unique_slices(word: str) -> list:
    return list(set(get_slices(word)))

# Strip newlines from each line in a file (for bonuses)
def read_words(file: object) -> list:
    return [ word.rstrip('\n') for word in file.readlines() ]

# Filter the words from enable1.txt to only candidates that make sense
def get_candidates(length: int, words: list) -> list:
    return [ x for x in words if len(x) == length ]

# Open our file for bonuses

enable1 = open('../../resources/enable1.txt')
wordlist = read_words(enable1)

# Start execution of the challenge

print('Challenge:')

for key in CHALLENGE_INPUT:
    print('funnel("' + key + '", "' + CHALLENGE_INPUT[key] + '") => '
        + ('true' if funnel(key, CHALLENGE_INPUT[key]) else 'false'))

# # Bonus 1 algorithm

def bonus(word: str) -> list:
    matches = [ x for x in get_unique_slices(word) if x in get_candidates(len(word) - 1, wordlist) ]
    return matches

# Bonus 2 algorithm
def bonus2(word: str) -> bool:
    if len(word) < BONUS2_INPUT:
        return False
    slices = get_slices(word)
    if len(slices) < 5:
        return False
    matches = 0
    candidates = get_candidates(len(word) - 1, wordlist)
    for c in candidates:
        if c in slices:
            matches = matches + 1
    return matches == BONUS2_INPUT

# Start execution of bonus 1

print('Bonus 1:')

for word in BONUS1_INPUT:
    output = 'bonus("' + word + '") => ['

    result = bonus(word)
    for r in result:
        output = output + '"' + r + '", '

    output = output.rstrip(', ') + ']'
    print(output)

# Start execution of bonus 2

print('Bonus 2:')

results = [ word for word in wordlist if bonus2(word)]

for k in results:
    print(k)

# End execution

enable1.close()
input()