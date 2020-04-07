# Create by Kyrill Chornokozynsky
import os
import re


class TwoWordIndex:
    def __init__(self, directory):
        self.__directory = os.listdir(directory);
        self.__mat_incidence = {}
        self.__inverted_indexes = {}
        self.__biwords_number = 0
        self.fill_info(directory)

    def fill_info(self, path):

        for file in self.__directory:
            # print(file)
            txt = open(path + "\\" + file, 'r', encoding="utf-8")
            biword_place = 0;
            temp = None
            for line in txt:
                biwords = re.findall('([a-zа-я]+\'?[a-zа-я]*)', line.lower())
                if len(biwords) == 0:
                    continue
                if temp is not None:
                    self.__biwords_number += 1
                    biword_place += 1
                    biword = temp + " " + biwords[0];

                    if self.__mat_incidence.get(biword) is None:
                        values = [0] * len(self.__directory)
                        self.__mat_incidence.update({biword: values})

                    self.__mat_incidence.get(temp + " " + biwords[0])[self.__directory.index(file)] = 1
                    if self.__inverted_indexes.get(biword) is None:
                        self.__inverted_indexes.update({biword: {file: [biword_place]}})
                    elif file not in self.__inverted_indexes.get(biword).keys():
                        self.__inverted_indexes.get(biword).update({biword: {file: [biword_place]}})
                    else:
                        self.__inverted_indexes.get(biword).get(file).append(biword_place)

                for i in range(0, len(biwords) - 1):
                    biword = biwords[i] + " " + biwords[i + 1]

                    self.__biwords_number += 1
                    biword_place += 1
                    if self.__mat_incidence.get(biword) is None:
                        values = [0] * len(self.__directory)
                        self.__mat_incidence.update({biword: values})

                    self.__mat_incidence.get(biword)[self.__directory.index(file)] = 1
                    if self.__inverted_indexes.get(biword) is None:
                        self.__inverted_indexes.update({biword: {file: [biword_place]}})
                    elif file not in self.__inverted_indexes.get(biword).keys():
                        self.__inverted_indexes.get(biword).update({file: [biword_place]})
                    else:
                        self.__inverted_indexes.get(biword).get(file).append(biword_place)
                temp = biwords[-1]

            txt.close()

    def write_info(self, path):
        dict = open(path, "w", encoding="utf-8")
        for word in self.__inverted_indexes.keys():
            dict.write(
                word + ", " + "%s" % self.__mat_incidence.get(word) + ", " + "%s\n" % self.__inverted_indexes.get(word))
        dict.close()

    @property
    def mat_incidence(self):
        return self.__mat_incidence

    @property
    def inverted_indexes(self):
        return self.__inverted_indexes

    @property
    def directory(self):
        return self.__directory

    @property
    def biwords_number(self):
        return self.__biwords_number


if __name__ == "__main__":
    diu = TwoWordIndex("D:/information-retrieval-project/res");
    diu.write_info("D:/information-retrieval-project/out/out.txt")
