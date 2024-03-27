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


def __parseparams(pattern, keep_ltrs, elim_ltrs, elim_pattern: list = ['zzzzz']) -> tuple:
    ptrn = pattern.lower()
    in_ltrs = keep_ltrs.lower()
    ex_ltrs = elim_ltrs.lower()

    if len(pattern) != 5:
        raise ValueError("The RegEx pattern must be 5 characters long")

    for c in pattern:
        if c not in '.abcdefghijklmnopqrstuvwxyz':
            raise ValueError("Your pattern contains characters other than . or a-z")

    try:
        re.compile(pattern)
    except re.error:
        raise ValueError("Your match pattern is not a valid regex pattern")

    for excl_pattern in elim_pattern:
        try:
            re.compile(excl_pattern)
        except re.error:
            raise ValueError("One of your elimination pattern(s) is not a valid regex pattern")

    for c in ex_ltrs:
        if c in pattern:
            msg: str = f"Your pattern contains one of the elimination characters: {pattern} --> {str().join(sorted(ex_ltrs))}"
            raise ValueError(msg)
        if c in in_ltrs:
            msg: str = f"Your keep letter(s) contain one of the elimination characters: {str().join(sorted(in_ltrs))} --> {str().join(sorted(ex_ltrs))}"
            raise ValueError(msg)
    return ptrn, in_ltrs, ex_ltrs, elim_pattern


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


def matchunusedwords(pattern: str, keep_ltrs: str = '', elim_ltrs: str = '', elim_pattern: str = 'zzzzz') -> tuple:
    """Given a RegEx pattern and a string of eliminated letters,
        return matching words from the valid Wordle word list
        that have not yet been used"""

    possible_words, most_common_ltrs = matchwords(pattern, keep_ltrs, elim_ltrs, elim_pattern, unused=True)

    return possible_words, most_common_ltrs


def matchwords(pattern: str, keep_ltrs: str = '', elim_ltrs: str = '', elim_pattern: list = ['zzzzz'], unused: bool = False) -> tuple:
    """Given a RegEx pattern and a string of eliminated letters,
        return matching words from the valid Wordle word list"""

    ptrn, in_ltrs, ex_ltrs, elim_ptrn = __parseparams(pattern, keep_ltrs, elim_ltrs, elim_pattern)
    word_lists = __readfiles()
    valid_words, used_words = word_lists[0], word_lists[1]
    if unused == True:
        valid_words = [word for word in valid_words if word not in used_words]
    match_words = [word for word in valid_words if (re.search(ptrn, word) is not None)]
    for excl_pattern in elim_pattern:
        drop_words =  [word for word in match_words if (re.search(excl_pattern, word) is not None)]
        match_words = [word for word in match_words if (word not in drop_words)]

    matching_words = _findmatchingwords(match_words, in_ltrs, ex_ltrs)

    counts = Counter()
    for word in matching_words:
        counts.update(word)

    return matching_words, counts.most_common(5)


if __name__ == '__main__':
    from wordleHelper import matchunusedwords as muw
    from wordleHelper import matchwords as mw

    # p = 's.l..'
    # k = ''
    # t = 'ternfoic'
    # ep = ['.u...']
    # matches, common_ltrs = matchwords(p, k, t, ep)
    # print('')
    # print(matches)
    # print(common_ltrs)
    # print('')
    # possibles, common_ltrs = matchunusedwords(p, k, t, ep)
    # print(possibles)
    # print(common_ltrs)

    print('')
    print("w, c = mw('.....', '', ''); print(w); print(len(w)); print(c);")
    print("w, c = muw('.....', '', ''); print(w); print(len(w)); print(c);")
