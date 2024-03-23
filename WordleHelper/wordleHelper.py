import sys
import re
import pandas as pd

# Create self-reference to module
this = sys.modules[__name__]

this.used_words = list()
this.valid_words = list()


def readfiles():
    raw_df = pd.read_csv(
                "https://raw.githubusercontent.com/bdwalker1/UCSD_ML_Bootcamp/main/WordleHelper/wordle_valid_words.txt"
                )
    this.valid_words = list(raw_df['valid_word'])
    del raw_df
    raw_df = pd.read_csv(
                "https://raw.githubusercontent.com/bdwalker1/UCSD_ML_Bootcamp/main/WordleHelper/wordle_used_words.txt"
                )
    this.used_words = list(raw_df['used_word'])
    del raw_df


def parseparams(pattern, keep_ltrs, elim_ltrs) -> tuple:
    ptrn = pattern.lower()
    in_ltrs = keep_ltrs.lower()
    ex_ltrs = elim_ltrs.lower()

    if len(pattern) != 5:
        raise ValueError("The RegEx pattern must be 5 characters long")

    for c in ex_ltrs:
        if c in pattern:
            raise ValueError("Your pattern contains one of the elimination characters")
    return ptrn, in_ltrs, ex_ltrs


def findmatchingwords(wordlist, keep_ltrs, elim_ltrs) -> list:
    matches = list()
    for word in wordlist:
        word_good: bool = True
        for c in elim_ltrs:
            if c in word:
                word_good = False
                break
        for c in keep_ltrs:
            if c not in word:
                word_good = False
                break
        if word_good:
            matches.append(word)
    return matches


def matchunusedwords(pattern: str, keep_ltrs: str = '', elim_ltrs: str = '') -> list:
    """Given a RegEx pattern and a string of eliminated letters,
        return matching words from the valid Wordle word list
        that have not yet been used"""

    ptrn, in_ltrs, ex_ltrs = parseparams(pattern, keep_ltrs, elim_ltrs)
    readfiles()
    unused_words = [word for word in this.valid_words if word not in this.used_words]
    match_words = [word for word in unused_words if re.search(ptrn, word) is not None]
    possible_words = findmatchingwords(match_words, in_ltrs, ex_ltrs)

    return possible_words


def matchwords(pattern: str, keep_ltrs: str = '', elim_ltrs: str = '') -> list:
    """Given a RegEx pattern and a string of eliminated letters,
        return matching words from the valid Wordle word list"""

    ptrn, in_ltrs, ex_ltrs = parseparams(pattern, keep_ltrs, elim_ltrs)
    readfiles()
    match_words = [word for word in this.valid_words if re.search(ptrn, word) is not None]

    matching_words = findmatchingwords(match_words, in_ltrs, ex_ltrs)

    return matching_words


if __name__ == '__main__':
    p = 'ab...'
    k = 'o'
    t = 'url'
    print(matchwords(p, k, t))
    print(matchunusedwords(p, k, t))
