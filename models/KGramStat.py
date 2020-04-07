class KGramStat:

    def __init__(self):
        self.__inverted_indexes = {}

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

    @property
    def inverted_indexes(self):
        return self.__inverted_indexes
