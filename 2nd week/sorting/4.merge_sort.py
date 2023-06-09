# it uses divide and conquer so, it is a recursive algorithm.,merge is done in post order traversal.
#     Algorithm:   ( Abdul Bari: youtube channel)
# MergeSort(l,h)
# {
#     if (l<h)
#     {
#         mid=(l+h)/2;
#         MergeSort(l,mid);
#         MergeSort(mid+1,h);
#         Merge(l,mid,h)
#     }
# }


def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
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

# time complexity for divide = O(log n)  and put it back=O(n) ,total=O(n log n)
# space O(n)
