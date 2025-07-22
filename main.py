import sys
from stats import stats_main

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)
path = sys.argv[1] 

def get_book_text(relative_path):
    with open(relative_path) as f:
        return f.read()
    # do something with f (the file) here

def main(path):
    text = get_book_text(path)
    num_words, lista = stats_main(text)
    # print(f"""{num_words} words found in the document""")
    linked = ""
    for entrada in lista:
        for valor in entrada:
            linked += valor + ": " + str(entrada[valor]) + "\n" + "    " 

    text = f"""============ BOOKBOT ============
    Analyzing book found at {path}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------
    {linked}
    ============= END ==============="""
    print(text)

main(path)