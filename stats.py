def sort_on(items):
    return items["value"]

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
    list1 = []

    for char in dict:
        list1.append({"char":char, "value":dict[char]})
    list1.sort(reverse=True, key=sort_on)
    list2 = []
    for entry in list1:
        list2.append({entry["char"]:entry["value"]})
    return list2
            
def stats_main(string):
    nw = count_words(string)
    dict_w = count_char(string)
    return nw, dict_w
