#!/usr/bin/env python

def main():
    test_list = [2, 4, 5, 3, 6, 1]
    assert bubble_sort(test_list) == sorted(test_list)
    test_list = [2]
    assert bubble_sort(test_list) == sorted(test_list)
    test_list = []
    assert bubble_sort(test_list) == sorted(test_list)

def bubble_sort(sortable_list):
    while True:
        swapped = False
        import ipdb; ipdb.set_trace()
        for index, value in enumerate(sortable_list[:-1]):
            if value > sortable_list[index + 1]:
                swapped = True
                swap = sortable_list[index + 1]
                sortable_list[index] = swap
                sortable_list[index + 1] = value
        if not swapped:
            break
    return sortable_list

if __name__ == "__main__":
    main()
