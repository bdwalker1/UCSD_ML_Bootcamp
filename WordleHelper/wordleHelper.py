import re
import pandas as pd
from collections import Counter

def __readfiles() -> list:
    raw_df = pd.read_csv(
                "https://raw.githubusercontent.com/bdwalker1/UCSD_ML_Bootcamp/main/WordleHelper/wordle_valid_words.txt"
                )
    valid_words = list(raw_df['valid_word'])
    del raw_df
    raw_df = pd.read_csv(
                "https://raw.githubusercontent.com/bdwalker1/UCSD_ML_Bootcamp/main/WordleHelper/wordle_used_words.txt"
                )
    used_words = list(raw_df['used_word'])
    del raw_df
    return [valid_words, used_words]


def __parseparams(pattern, keep_ltrs, elim_ltrs) -> tuple:
    ptrn = pattern.lower()
    in_ltrs = keep_ltrs.lower()
    ex_ltrs = elim_ltrs.lower()

    if len(pattern) != 5:
        raise ValueError("The RegEx pattern must be 5 characters long")

    for c in pattern:
        if c not in '.abcdefghijklmnopqrstuvwxyz':
            raise ValueError("Your pattern contains characters other than . or a-z")

    for c in ex_ltrs:
        if c in pattern:
            msg: str = f"Your pattern contains one of the elimination characters: {pattern} --> {str().join(sorted(ex_ltrs))}"
            raise ValueError(msg)
        if c in in_ltrs:
            msg: str = f"Your keep letter(s) contain one of the elimination characters: {str().join(sorted(in_ltrs))} --> {str().join(sorted(ex_ltrs))}"
            raise ValueError(msg)
    return ptrn, in_ltrs, ex_ltrs


def _findmatchingwords(wordlist, keep_ltrs, elim_ltrs) -> list:
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

    ptrn, in_ltrs, ex_ltrs = __parseparams(pattern, keep_ltrs, elim_ltrs)
    word_lists = __readfiles()
    valid_words, used_words = word_lists[0], word_lists[1]
    unused_words = [word for word in valid_words if word not in used_words]
    match_words = [word for word in unused_words if re.search(ptrn, word) is not None]
    possible_words = _findmatchingwords(match_words, in_ltrs, ex_ltrs)

    counts = Counter()
    for word in possible_words:
        counts.update(word)

    return possible_words, counts.most_common(5)


def matchwords(pattern: str, keep_ltrs: str = '', elim_ltrs: str = '') -> list:
    """Given a RegEx pattern and a string of eliminated letters,
        return matching words from the valid Wordle word list"""

    ptrn, in_ltrs, ex_ltrs = __parseparams(pattern, keep_ltrs, elim_ltrs)
    word_lists = __readfiles()
    valid_words, used_words = word_lists[0], word_lists[1]
    match_words = [word for word in valid_words if re.search(ptrn, word) is not None]

    matching_words = _findmatchingwords(match_words, in_ltrs, ex_ltrs)

    return matching_words


if __name__ == '__main__':
    p = '.o...'
    k = 'le'
    t = 'fi'
    print(matchwords(p, k, t))
    possibles, common_ltrs = matchunusedwords(p, k, t)
    print(possibles)
    print(common_ltrs)
