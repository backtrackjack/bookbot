def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    char_list = {}
    for char in text:
        lower = char.lower()
        if lower in char_list:
            char_list[lower] += 1
        else:
            char_list[lower] = 1
    return char_list


def sort_on(dict):
    return dict["count"]


def sorted_dict(dictionary):
    new_list = []
    for item in dictionary:
        new_list.append({"character": item, "count": dictionary[item]})
    new_list.sort(key=sort_on, reverse=True)
    return new_list
