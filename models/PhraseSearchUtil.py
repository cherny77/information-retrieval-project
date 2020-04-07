# Create by Kyrill Chornokozynsky
import os
import re

from models.BoolCalculator import and_oper, mat_to_books


def line_to_biwords(line):
    line = re.split(" ", line.lower())
    biwords = []
    for i in range(0, len(line) - 1):
        biwords.append(line[i] + " " + line[i + 1])
    return biwords


def find_phrase_by_biwords(line, mat_incidence, directory):
    biwords = line_to_biwords(line)
    for biword in biwords:
        biwords[biwords.index(biword)] = mat_incidence.get(biword)

    while len(biwords) != 1:
        if biwords[0] is None:
            biwords[0] = [0 * len(directory)]
        if biwords[1] is None:
            biwords[1] = [0 * len(directory)]

        biwords[1] = and_oper(biwords[0], biwords[1])
        del biwords[0]
    return mat_to_books(biwords[0], directory)


def find_phrase_by_words(line, mat_incidence, inverted_indexes, directory):
    line = re.split(" ", line.lower())
    incidences = []
    words = []
    spaces = [None]
    res = set()
    i = 0
    while i < len(line):
        incidences.append(mat_incidence.get(line[i]))
        words.append(line[i])
        i += 2
        if i < len(line):
            spaces.append((int)(line[i - 1][1:]))

    while len(incidences) != 1:
        incidences[1] = and_oper(incidences[0], incidences[1])
        del incidences[0]
    if mat_to_books(incidences[0], directory) is None:
        return None
    else:
        files = []

        for i in range(len(incidences[0])):
            if incidences[0][i] == 1:
                files.append(i)

    for file in files:
        for space in inverted_indexes.get(words[0]).get(directory[file]):
            is_here = True
            spaces_sum = 0;
            for i in range(1, len(words)):
                spaces_sum += spaces[i]
                if (space + spaces_sum) + i not in inverted_indexes.get(words[i]).get(directory[file]):
                    is_here = False
                    break
            if is_here:
                res.update([directory[file]])
    if len(res) == 0:
        return "No books!"
    return res
