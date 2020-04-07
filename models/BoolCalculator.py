import re


def and_oper(u, v):
    return list(set(list(u)).intersection(list(v)))


def or_oper(u, v):
    return list(set(list(u) + list(v)))


def not_oper(u, directory):
    return list(set(directory) - set(list(u)))


def bool_calculate(line, inverted_indexes, directory):
    line = re.split(" ", line.lower())
    operators = ["or", "and"]
    for item in line:

        if item not in operators:
            if item == "not":
                line[line.index(item) + 1] = not_oper(inverted_indexes[(line[line.index(item) + 1])].keys(), directory)
                line.remove(item)
            elif item not in inverted_indexes.keys():
                line[line.index(item)] = []

            else:
                line[line.index(item)] = inverted_indexes[item].keys()

    for i in range(0, len(line) - 1):
        if len(line) == i:
            break
        if line[i] == "and":
            line[i] = and_oper(line[i - 1], line[i + 1])
            del line[i - 1]
            del line[i]
            i = 0;

    for i in range(0, len(line) - 1):
        if len(line) == i:
            break
        if line[i] == "or":
            line[i] = or_oper(line[i - 1], line[i + 1])
            del line[i - 1]
            del line[i]
            i = 0;

    return line[0]
