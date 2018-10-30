# [2018-08-22] Challenge #366 [Intermediate] Word funnel 2
# https://www.reddit.com/r/dailyprogrammer/comments/99d24u/20180822_challenge_366_intermediate_word_funnel_2/

# Strip newlines from each line in a file (for bonuses)
def read_words(file: object) -> list:
    return [ word.rstrip('\n') for word in file.readlines() ]

# Start with our wordlist

enable1 = open('../../resources/enable1.txt')
wordlist = read_words(enable1)

# Our funnel algorithm from 2018-08-20_easy bonus 1
def funnel(word: str) -> list:
    matches = [ x for x in get_slices(word) if x in wordlist ]
    return matches

# Return all strings that are missing one letter
def get_slices(word: str) -> list:
    return [ word[:i] + word[i+1:] for i, c in enumerate(word) ]


# A word funnel is a tree.
class tree(object):

    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.children = []
        self.set_childen()
        print('P:' + (parent.value.ljust(10) if self.parent else 'NONE      ')
            + ' V:' + value.ljust(10)
            + ' L:' + ('Y' if self.is_leaf() else ''))

    def set_childen(self):
        for w in funnel(self.value):
            self.children.append(tree(w, self))

    def add_child(word: str):
        self.children.append(tree(word, self))

    def is_root(self) -> bool:
        return self.parent is None

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def depth(self) -> int:
        if self.parent:
            return 1 + self.parent.depth()
        else:
            return 1

    def path(self) -> list:
        if self.parent:
            return self.parent.path().append(self)
        else:
            return []

    def leaf_depths(self) -> dict:
        return { leaf: leaf.depth() for leaf in self.get_leaves() }

    def get_leaves(self) -> list:
        leaves = []
        self.add_leaves(leaves)
        leaves = [ l for l in leaves if l is not None ]
        return leaves

    def add_leaves(self, leaves):
        if self.is_leaf():
            return self
        else:
            leaves.extend([ child.add_leaves(leaves) for child in self.children ])









while True:
    word = input('Word or EXIT: ')
    if word == 'EXIT':
        break
    word_tree = tree(word)





# End execution

enable1.close()
input()