from models.SingleWordIndex import SingleWordIndex
from models.BoolCalculator import bool_calculate

if __name__ == "__main__":
    swi = SingleWordIndex("D:/information-retrieval-project/res");
    swi.write_info("D:/information-retrieval-project/out/out.txt")
    print("edit or where : ", bool_calculate("not edit or where", swi.inverted_indexes, swi.directory))
    print("edit and where : ", bool_calculate("edit and where", swi.inverted_indexes, swi.directory))