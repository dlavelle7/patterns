#!/usr/bin/env python

def main():
    test_list = [2, 4, 5, 3, 6, 1]
    assert bubble_sort(test_list) == sorted(test_list)
    test_list = [2]
    assert bubble_sort(test_list) == sorted(test_list)
    test_list = []
    assert bubble_sort(test_list) == sorted(test_list)
    test_list = [2, 4, 5, 3, 2, 1]
    assert bubble_sort(test_list) == sorted(test_list)
    test_list = [2, 4, 5, 3, 3, 1]
    assert bubble_sort(test_list) == sorted(test_list)
    test_list = [8, 8, 8, 5, 3, 1, 1]
    assert bubble_sort(test_list) == sorted(test_list)

def bubble_sort(sortable_list):
    while True:
        swapped = False
        for index in range(len(sortable_list) -1):
            if sortable_list[index] > sortable_list[index + 1]:
                swapped = True
                swap_a = sortable_list[index + 1]
                swap_b = sortable_list[index]
                sortable_list[index] = swap_a
                sortable_list[index + 1] = swap_b
        if not swapped:
            break
    return sortable_list

if __name__ == "__main__":
    main()
