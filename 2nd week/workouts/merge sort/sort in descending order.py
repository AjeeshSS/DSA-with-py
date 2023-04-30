def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


# print(merge([1,1,1,2,7,8],[1,3,4,5,6]))

def merge_sort(List):
    if len(List) == 1:
        return List
    mid_index = len(List) // 2  # floor division ,divides and rounded down to the nearest integer.
    left = merge_sort(List[:mid_index])  # recursive function
    right = merge_sort(List[mid_index:])  # recursive function

    return merge(left, right)


list = [1, 2, 3, 4, 5, 67, 4, 232, 4, 2]
print(list)
print('\n after merge \n', merge_sort(list))
