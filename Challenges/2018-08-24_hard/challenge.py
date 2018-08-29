# [2018-08-24] Challenge #366 [Hard] Incomplete word ladders
# https://www.reddit.com/r/dailyprogrammer/comments/99yl83/20180824_challenge_366_hard_incomplete_word/

# I've written a greedy solution.

# Challenge parameters
MAX_SPACING = 100
test_file = open('363-hard-words.txt')

# Return the spacing between two strings (see Definitions) 
def spacing(a: str, b: str) -> int:
    assert len(a) == len(b)

    i = 0
    count = 0

    while i < len(a):
        if a[i] != b[i]:
            count = count + 1
        i = i + 1

    return count - 1 # Words that are adjacent have a spacing of 0.

# Find the spacing from a word to each other word in the dict
def find_spacing(word: str, words: list) -> dict:
    result = { candidate : spacing(word, candidate) for candidate in words}
    return result

# Strip newlines from each line in a file
def read_words(file: object) -> list:
    return [ word.rstrip('\n') for word in file.readlines() ]

# Find the key with the minimum value in our dict
# See https://stackoverflow.com/a/12343826
def find_choice(candidates: dict) -> str:
    return min(candidates, key=candidates.get)

# Start execution of the challenge itself

test_words = read_words(test_file)
current_word = test_words.pop(0)
solution = {current_word: 0}
running = True

while running:
    candidates = find_spacing(current_word, test_words)
    choice = find_choice(candidates)
    if len(test_words) == 1 or sum(solution.values()) + candidates[choice] > MAX_SPACING:
        running = False
        break
    else:
        solution[choice] = candidates[choice]
        current_word = test_words.pop(test_words.index(choice))

for k in solution:
    print(k, solution[k])

print('Output length:', len(solution))
print('Total spacing:', sum(solution.values()))

# End execution
test_file.close()
input()
