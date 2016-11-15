#!/usr/bin/env python3

from difflib import SequenceMatcher
from itertools import zip_longest


def is_junk(char):
    return char in ' \t'


def similarity(line1, line2):
    return SequenceMatcher(is_junk, line1, line2).ratio()


def remove_blanks(lines):
    return [line for line in lines if line.strip() != '']


def similar_texts(text1, text2, line_sim_thrs=0.6):
    lines1, lines2 = remove_blanks(text1.split('\n')), remove_blanks(text2.split('\n'))
    similarities = (similarity(l1, l2) for l1, l2 in zip_longest(lines1, lines2, fillvalue=''))
    num_similar = len([s for s in similarities if s > line_sim_thrs])
    return num_similar > (min(len(lines1), len(lines2)) // 2)