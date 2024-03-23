import sys
import csv
import re

# Create self-reference to module
this = sys.modules[__name__]

this.used_words = list()
this.valid_words = list()


def readfiles():

    file = open("wordle_valid_words.txt", "r")
    this.valid_words = list(csv.reader(file, delimiter=","))
    file.close()
    file = open("wordle_used_words.txt", "r")
    this.used_words = list(csv.reader(file, delimiter=","))
    file.close()
    del file

    this.used_words.pop(0)
    this.valid_words.pop(0)


def matchunusedwords(pattern: str, keep_ltrs:str = '', elim_ltrs: str = '') -> list:
    """Given a RegEx pattern and a string of eliminated letters,
        return matching words from the valid Wordle word list
        that have not yet been used"""
    ptrn = pattern.lower()
    in_ltrs = keep_ltrs.lower()
    ex_ltrs = elim_ltrs.lower()

    if len(pattern) != 5:
        raise ValueError("The RegEx pattern must be 5 characters long")

    for c in ex_ltrs:
        if c in pattern:
            raise ValueError("Your pattern contains one of the elimination characters")

    readfiles()
    possible_words = []
    unused_words = [word for word in this.valid_words if word not in this.used_words]
    match_words = [word[0] for word in unused_words if re.search(ptrn, word[0]) is not None]

    for word in match_words:
        word_good: bool = True
        for c in ex_ltrs:
            if c in word:
                word_good = False
                break
        for c in in_ltrs:
            if c not in word:
                word_good = False
                break
        if word_good:
            possible_words.append(word)

    return possible_words


def matchwords(pattern: str, keep_ltrs:str = '', elim_ltrs: str = '') -> list:
    """Given a RegEx pattern and a string of eliminated letters,
        return matching words from the valid Wordle word list"""
    ptrn = pattern.lower()
    in_ltrs = keep_ltrs.lower()
    ex_ltrs = elim_ltrs.lower()

    if len(ptrn) != 5:
        raise ValueError("The RegEx pattern must be 5 characters long")

    for c in ex_ltrs:
        if c in ptrn:
            raise ValueError("Your pattern contains one of the elimination characters")

    readfiles()
    match_words = [word[0] for word in this.valid_words if re.search(ptrn, word[0]) is not None]

    matching_words = []
    for word in match_words:
        word_good: bool = True
        for c in ex_ltrs:
            if c in word:
                word_good = False
                break
        for c in in_ltrs:
            if c not in word:
                word_good = False
                break
        if word_good:
            matching_words.append(word)

    return matching_words


if __name__ == '__main__':
    p = 'ab...'
    k = 'o'
    t = 'url'
    print(matchwords(p, k, t))
    print(matchunusedwords(p, k, t))
