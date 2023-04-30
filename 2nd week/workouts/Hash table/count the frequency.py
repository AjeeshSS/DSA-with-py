def frequency(words):
    dict_table = {}
    for i in words:
        if i in dict_table:
            dict_table[i] += 1
        else:
            dict_table[i] = 1
    return dict_table


print(frequency("hhohpodud"))
