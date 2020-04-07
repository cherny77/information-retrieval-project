import re



def and_oper(u, v):
    res = [0] * len(u)
    for i in range(0, len(u)):
        res[i] = u[i] and v[i]
    return res


def or_oper(u, v):
    res = [0] * len(u)
    for i in range(0, len(u)):
        res[i] = u[i] or v[i]
    return res


def not_oper(u):
    res = [0] * len(u)
    for i in range(0, len(u)):
        if u[i] == 1:
            res[i] = 0
        else:
            res[i] = 1
    return res


def mat_to_books(u, directory):
    books = set()
    for i in range(0, len(u)):

        if u[i] == 1:
            books.update([directory[i]])
    if len(books) == 0:
        return "No books!"
    return books;


def bool_calculate(line, mat_incidence, directory):
    line = re.split(" ", line.lower())
    operators = ["or", "and"]
    for item in line:

        if item not in operators:
            if item == "not":
                line[line.index(item) + 1] = not_oper(mat_incidence.get(line[line.index(item) + 1]))
                line.remove(item)
            elif item not in mat_incidence.keys():
                line[line.index(item)] = [0] * len(directory)

            else:
                line[line.index(item)] = mat_incidence.get(item)

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

    return mat_to_books(line[0], directory)
