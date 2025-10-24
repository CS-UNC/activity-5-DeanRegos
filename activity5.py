words_file = open('CROSSWD.txt', 'r')

# # Function 1
def more_than_20(file):
    data = []
    for x in words_file:
        if len(x) >= 22:
            x1 = x.replace("\n", "")
            data.append(x1)
    return data

print(more_than_20(words_file))


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
    # all_words_file = open('CROSSWD.txt', 'r')
    data1 = []
    for word in file:
        if uses_only(word, letters) == True:
            data1.append(word)
    print(data1)

# all_uses_only('CROSSWD.txt', 'abrz')