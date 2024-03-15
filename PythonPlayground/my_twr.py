import pandas as pd
# import numpy as np

pegs = [[], [], []]


def mv_twr(h: int, peg1: str, peg2: str, peg3: str) -> int:
    if h == 0:
        return 0
    elif h == 1:
        print(f'From {peg1} to {peg3}')
    else:
        mv_twr(h - 1, peg1, peg3, peg2)
        mv_twr(1, peg1, peg2, peg3)
        mv_twr(h - 1, peg2, peg1, peg3)


def show_pegs() -> None:
    peg_df = pd.DataFrame(pegs).T.iloc[::-1]
    for i, row in peg_df.iterrows():
        print(f'{str(row[0] or ''): ^5}{str(row[1] or ''): ^5}{str(row[2] or ''): ^5}')
    print(f'---------------')


def mv_twr2(h: int, from_peg: int, mid_peg: int, to_peg: int) -> int:
    steps: int = 0
    if (len(pegs[0]) == 0) & (len(pegs[1]) == 0) & (len(pegs[2]) == 0) & (h > 0):
        for i in range(h):
            pegs[0].append(chr(ord('A') + (h-i-1)))
        show_pegs()
    if h == 0:
        return 0
    elif h == 1:
        # print('From {from_peg} to {to_peg}')
        pegs[to_peg].append(pegs[from_peg][len(pegs[from_peg])-1])
        del pegs[from_peg][len(pegs[from_peg]) - 1]
        show_pegs()
        return 1
    else:
        steps = steps + mv_twr2(h - 1, from_peg, to_peg, mid_peg)
        steps = steps + mv_twr2(1, from_peg, mid_peg, to_peg)
        steps = steps + mv_twr2(h - 1, mid_peg, from_peg, to_peg)
        return steps


if __name__ == '__main__':
    # mv_twr(7, 'a', 'b', 'c')
    moves: int = mv_twr2(3, 0, 1, 2)
    print(f'Solved in {moves} moves.')
    pegs = [[], [], []]
    moves: int = mv_twr2(4, 0, 1, 2)
    print(f'Solved in {moves} moves.')
