# Create by Kyrill Chornokozynsky
import os
import re


class SingleWordIndex:

    def __init__(self, directory):
        self.__directory = os.listdir(directory);
        self.__inverted_indexes = {}
        self.__mat_incidence = {}
        self.__words_number = 0;
        self.fill_info(directory)

    def fill_info(self, path):

        for file in self.__directory:
            # print(file)
            txt = open(path + "\\" + file, 'r', encoding="utf-8")
            for line in txt:
                words = re.findall('([a-zа-я]+\'?[a-zа-я]+)', line.lower())
                for word in words:
                    self.__words_number += 1
                    if self.__mat_incidence.get(word) is None:
                        values = [0] * len(self.__directory);
                        self.__mat_incidence.update({word: values})

                    self.__mat_incidence.get(word)[self.__directory.index(file)] = 1
                    if self.__inverted_indexes.get(word) == None:
                        self.__inverted_indexes.update({word: {file: [self.__words_number]}})
                    elif file not in self.__inverted_indexes.get(word):
                        self.__inverted_indexes.get(word).update({file: [self.__words_number]})
                    else:
                        self.__inverted_indexes.get(word).get(file).append(self.__words_number)

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
    def words_number(self):
        return self.__words_number


if __name__ == "__main__":
    diu = SingleWordIndex("D:/information-retrieval-project/res");
    for word in diu.inverted_indexes.keys():
        print(diu.inverted_indexes[word].keys())
    diu.write_info("D:/information-retrieval-project/out/out.txt")
