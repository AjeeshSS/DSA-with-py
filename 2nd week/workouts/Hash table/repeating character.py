def repeat(word, x):
    count_dict = {}

    for i in word:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

        if count_dict[i] == x:
            print(i)


repeat("hhoh0oew344", 2)
