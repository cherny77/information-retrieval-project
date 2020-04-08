from models.KGramStat import KGramStat
from models.SingleWordIndex import SingleWordIndex
from models.SwappedIndex import SwappedIndex
from models.Trie import Trie

if __name__ == '__main__':
    # By k-grams
    swi = SingleWordIndex("D:/information-retrieval-project/res")
    # kgs = KGramStat(list(swi.inverted_indexes.keys()))
    # print("*а*сказ*ва* : ", kgs.search("*а*сказ*ва*"))
    # print("park* : ", kgs.search("park*"))
    # print("*ant* : ", kgs.search("*ant*"))
    # print("po* : ", kgs.search("po*"))
    #
    # # By swapped index
    si = SwappedIndex(list(swi.inverted_indexes.keys()))
    # print("park* : ", si.search("park*"))
    print("po* : ", si.search("po*"))

    # By trie
    trie = Trie(list(swi.inverted_indexes.keys()))
    print("po* : ", trie.search("po*"))
