def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def SelectionSort(lst):
    min_idx = 0
    for start in range(0, len(lst) - 1):
        min_idx = start
        for idx in range(min_idx+1, len(lst)):
            if lst[min_idx] > lst[idx]:
                swap(lst, min_idx, idx)

    return lst

print(SelectionSort([77, 6, 4, 3, 2, 21, 999]))
