# Create by Kyrill Chornokozynsky
import os
import re

from models.BoolCalculator import and_oper


def line_to_biwords(line):
    line = re.split(" ", line.lower())
    biwords = []
    for i in range(0, len(line) - 1):
        biwords.append(line[i] + " " + line[i + 1])
    return biwords


def find_phrase_by_biwords(line, inverted_indexes, directory):
    biwords = line_to_biwords(line)
    for biword in biwords:
        if biword in inverted_indexes:
            biwords[biwords.index(biword)] = inverted_indexes[biword].keys()
        else:
            biwords[biwords.index(biword)] = []
    while len(biwords) > 1:
        biwords[0] = and_oper(biwords[0], biwords[1])
        del biwords[1]
    return biwords[0]


def find_phrase_by_words(line, inverted_indexes, directory):
    line = re.split(" ", line.lower())
    incidences = []
    words = []
    spaces = [None]
    res = set()
    i = 0
    while i < len(line):
        incidences.append(inverted_indexes[(line[i])].keys())
        words.append(line[i])
        i += 2
        if i < len(line):
            spaces.append((int)(line[i - 1][1:]))

    while len(incidences) != 1:
        incidences[1] = and_oper(incidences[0], incidences[1])
        del incidences[0]
    if incidences[0] is None:
        return None
    else:
        files = incidences[0]
    for file in files:
        for space in inverted_indexes[words[0]][file]:
            is_here = True
            spaces_sum = 0;
            for i in range(1, len(words)):
                spaces_sum += spaces[i]
                if (space + spaces_sum) + i not in inverted_indexes[words[i]][file]:
                    is_here = False
                    break
            if is_here:
                res.update([file])
    return res
