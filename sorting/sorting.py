#Bubble Sort

def bubble_sort(l):
    is_sorted = False

    while is_sorted is False:
        is_sorted = True

        for i in range(len(l)-1):
            num1, num2 = l[i], l[i+1]

            if num1 > num2:
                is_sorted = False
                l[i], l[i+1] = num2, num1

        print l

# bubble_sort([6, 2, 16, 0, -1])

#Merge Sort

def merge_sort(lst):

    """Merge sort list and return result."""

    print "calling merge_sort on", lst

    # Break everything down into a list of one
    if len(lst) < 2:  # if length of lst is 1, return lst
        print "returning", lst
        return lst

    mid = int(len(lst) / 2)  # index at half the list
    lst1 = merge_sort(lst[:mid])  # divide list in half
    lst2 = merge_sort(lst[mid:])  # assign other half

    # Compare first items of each pair of lists and interleaving a result list
    results = []
    print lst1, lst2

    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            results.append(lst2.pop(0))
        elif lst2 == []:
            results.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            results.append(lst1.pop(0))
        else:
            results.append(lst2.pop(0))
    print results
    return results

merge_sort([1, 6, 0, 3, 5, 4, -20, 7])

