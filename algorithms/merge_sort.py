#!/usr/bin/env python

def main():
    test_list = [5, 3, 6]
    assert merge_sort(test_list) == sorted(test_list)
    test_list = [2, 4, 5, 3, 6, 1]
    assert merge_sort(test_list) == sorted(test_list)
    test_list = [2]
    assert merge_sort(test_list) == sorted(test_list)
    test_list = []
    assert merge_sort(test_list) == sorted(test_list)
    test_list = [2, 4, 5, 3, 2, 1]
    assert merge_sort(test_list) == sorted(test_list)
    test_list = [2, -4, -5, 3, -3, 1]
    assert merge_sort(test_list) == sorted(test_list)

def merge_sort(sequence):
    if len(sequence) > 1:
        mid = len(sequence) / 2
        left = sequence[:mid]
        right = sequence[mid:]

        merge_sort(left)
        merge_sort(right)
        # left and right now sorted (single element lists)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sequence[k]=left[i]
                i=i+1
            else:
                sequence[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            sequence[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            sequence[k]=right[j]
            j=j+1
            k=k+1

    return sequence


if __name__ == "__main__":
    main()
