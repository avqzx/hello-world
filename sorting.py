def main():
    # nums = [ 77, 42, 35, 12, 101, 5 ]
    # nums = [ 5, 3, 8, 2, 1, 7, 4 ]
    nums = [5, 8, 3, 7, 1]
    bubble_sort(nums)
    # nums = [ 5, 1, 3, 6, 4, 6, 2 ]
    # nums = [ 5, 3, 8, 2, 1, 7, 4 ]
    nums = [5, 8, 3, 7, 1]
    selection_sort(nums)

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def selection_sort(nums):
    print nums
    N = len(nums)

    for i in range(N-1):
        """
        # below doesn't work because the min_index returned is only valid
        # for the shorter list given to get_min_index, and cannot be used
        # directly on the full list. Instead, we need to pass the full list
        # and the starting element to consider, in which case, this is no
        # different from the original approach of finding max and swapping with
        # the last unsorted element
        min_index = get_min_index(nums[i:])
        """

        """
        # working code for swapping min instead of max
        min_index = get_min_index(nums, i)
        # print "## i = {}, min_index = {}".format(i, min_index)
        swap(nums, min_index, i)
        """

        max_index = get_max_index(nums, N-i)
        # print "## i = {}, max_index = {}".format(i, max_index)
        swap(nums, max_index, N-1-i)

        if max_index != N-1-i:
            print nums

def get_min_index(nums, start):
    min_index = start
    for i in range(start+1, len(nums)):
        if nums[i] < nums[min_index]:
            min_index = i
    return min_index

def get_max_index(nums, length):
    max_index = 0
    for i in range(1, length):
        if nums[i] > nums[max_index]:
            max_index = i
    return max_index

def bubble_sort(nums):
    print nums

    length = len(nums)
    for i in range(1, length):
        for j in range(length - i):
            if nums[j] > nums[j+1]:
                swap(nums, j, j+1)
                print nums
        print

main()
