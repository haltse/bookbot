def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_dict(text):
    sort=[]
    chars = get_chars_dict(text)
    for k,v in chars.items():
        if k.isalpha():
            sort.append({"char":k ,"num": v})
    sort.sort(reverse=True, key=sort_on)

    return sort
