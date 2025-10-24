# # Function 1
def twenty_or_more(file):
    words_file = open('CROSSWD.txt', 'r')
    data = []
    for x in words_file:
        if len(x) > 21:
            x1 = x.replace("\n", "")
            data.append(x1)
    print(data)

# twenty_or_more('CROSSWD.txt')


# # Function 2
def has_no_e(word):
    check = True
    for letter in word:
        if 'e' == letter:
            check = False
    return check


# # Function 3
def uses_only(word, letters):
    for x in word:
        if x not in letters:
            return False
    return True

# print(uses_only('abra', 'abr'))


# # Function 4
def all_uses_only(file, letters):
    all_words_file = open('CROSSWD.txt', 'r')
    data1 = []
    for x in all_words_file:
        if uses_only(x, letters) == True:
            data1.append(x)
    print(data1)

# all_uses_only('CROSSWD.txt', 'abcdefg')