# swap a number in descending order

#swap
def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp


def pivot(list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if list[i] > list[pivot_index]:
            swap_index += 1
            swap(list, swap_index, i)
    swap(list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(list, left, right):
    if left < right:
        pivot_index = pivot(list, left, right)
        quick_sort_helper(list, left, pivot_index - 1)
        quick_sort_helper(list, pivot_index + 1, right)
    return list


def quick_sort(list1):
    return quick_sort_helper(list, 0, len(list) - 1)


list = [1, 2, 1, 3, 4, 78, 43, 8, 3]
print(quick_sort(list))
