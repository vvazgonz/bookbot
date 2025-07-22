

def count_words(string):
    words = string.split()
    return len(words)

def count_char(string):
    lower_string = string.lower()
    dict = {
    }
    for char in lower_string:
        if char not in dict:
            dict.update({char: 1})
        else:
            dict.update({char: dict[char]+1})
    
    list = []

    for char in dict:
        list.append({char: dict[char]})
    
    return list
            
def stats_main(string):
    nw = count_words(string)
    dict_w = count_char(string)
    return nw, dict_w
