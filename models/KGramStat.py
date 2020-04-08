import re

from models.BoolCalculator import and_oper


class KGramStat:

    def __init__(self):
        self.__inverted_indexes = {}

    def __init__(self, words):
        self.__inverted_indexes = {}
        self.fill(words)


    def add_word(self, word: str):
        e_word = "$" + word + "$"
        for i in range(0, len(e_word) - 2):
            kgram = e_word[i: i + 3]
            if kgram not in self.__inverted_indexes:
                self.__inverted_indexes.update({kgram: set([word])})
            else:
                self.__inverted_indexes.get(kgram).update([word])

    def fill(self, words):
        for word in words:
            self.add_word(word)

    def search(self, request):
        kgrams = []
        request_parts = re.split('\\*', request.lower())

        if request_parts[0] != "":
            request_parts[0] = "$" + request_parts[0]
        else:
            del request_parts[0]

        if request_parts[-1] != "":
            request_parts[-1] = request_parts[-1] + "$"
        else:
            del request_parts[-1]

        for part in request_parts:
            for i in range(0, len(part) - 2):
                kgrams.append(part[i: i + 3])

        for kgram in kgrams:
            if kgram in self.__inverted_indexes:
                kgrams[kgrams.index(kgram)] = self.__inverted_indexes[kgram]
            else:
                kgrams[kgrams.index(kgram)] = []


        while len(kgrams) > 1:
            kgrams[0] = and_oper(kgrams[0], kgrams[1])

            del kgrams[1]

        return kgrams[0];

    @property
    def inverted_indexes(self):
        return self.__inverted_indexes


if __name__ == '__main__':
    kgs = KGramStat()
    print(kgs.search("*loll*lol*aas"))
