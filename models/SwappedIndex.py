class SwappedIndex:
    def __init__(self):
        self.__inverted_index = {}

    def __init__(self, words):
        self.__inverted_index = {}
        self.fill(words)

    def fill(self, words):
        for word in words:
            self.add_word(word)

    def __request_to_swapped_index(self, request):
        request = request + "$"
        while (request[-1] != "*"):
            temp = request[0]
            request = request[1:]
            request += temp
        request = request[: -1]
        return request

    def add_word(self, word: str):
        swapped_forms = []
        swapped_word = word[1:] + "$" + word[0]
        if swapped_word not in swapped_forms:
            swapped_forms.append(swapped_word)
        while (swapped_word != word + "$"):
            swapped_word = swapped_word[1:] + swapped_word[0]
            if swapped_word not in swapped_forms:
                swapped_forms.append(swapped_word)
        self.__inverted_index[word] = swapped_forms

    def search(self, request):
        res = []
        request = self.__request_to_swapped_index(request)
        print(request)
        for word in self.__inverted_index.keys():
            for swapped_word in self.__inverted_index[word]:
                if request in swapped_word:
                    res.append(word)
                    break
        return res;

    @property
    def inverted_indexes(self):
        return self.__inverted_indexes

