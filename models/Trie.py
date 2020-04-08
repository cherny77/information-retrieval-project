class Trie:

    def __init__(self):
        self.__head = {}

    def __init__(self, words):
        self.__head = {}
        self.fill(words)

    @property
    def head(self):
        return self.__head

    def fill(self, words):
        for word in words:
            self.add(word)

    def add(self, word: str):
        cur = self.__head

        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = word

    def search(self, word):
        cur = self.__head
        if word[-1] == "*":
            word = word[: -1]
        for ch in word:
            if ch not in cur:
                return []
            cur = cur[ch]
        return self.words(cur)

    def words(self, cur):
        result = []
        for ch in cur:
            if ch == "*":
                result += [cur["*"]]
                continue
            result += self.words(cur[ch])
        return result


if __name__ == '__main__':
    trie = Trie()
    trie.add("po")
    trie.add("pa")
    print(trie.head)
