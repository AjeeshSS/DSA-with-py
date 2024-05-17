# it is a divide and conquer method,it splits large problem to sub problem and solves it.
# first letter is assumed as pivot element

# Algorithm:   ( Abdul Bari : youtube channel)
# partition(l,h)
# {
#     pivot=a[i];
#     i=l;
#     j=h;
#     while (i<j)
#     {
#         do
#         {
#             i++;
#         }
#         while (a[i]<=pivot)
#             do
#             {
#                 i--;
#             }
#             while (a[j]>pivot)
#             if (i<j)
#                 swap (a[i],a[j])
#     }
#     swap(a[l],a[j])
#     return j;
# }

# sort(l,h)
# {
#     if(l<h)
#     {
#         j=partition(l,h);
#         sort(l,j);
#         sort(j+1,h);
#     }
# }
#  there is a difference in algorithm and implementation ,but we get the logic.


# swap
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


# pivot
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)  # recursive
        quick_sort_helper(my_list, pivot_index + 1, right)  # recursive
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)


arr = ['a', 's', 'd', 'w', 'e', 'a', 'f', 'a', 'w']
print(quick_sort(arr))

list = [4, 6, 1, 7, 3, 2, 5]
print(quick_sort(list))

# to find  pivot, time comp O(n) + for recursive O(log n) = O(n log n)
#  if already sorted then O(n^2)  is the worst case
