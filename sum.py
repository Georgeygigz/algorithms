def sum_of_two_nums(array,target):
    """
    Given a target number and an array of
    numbers you are required to return the
    index of two numbers in array that sum up to
    the target number
    Args:
        array(list): list of input
        target(int): target value
    """
    nums = {}
    for i,num in enumerate(array):
        val = target - num
        if val in nums:
            return [nums[val], i]
        nums[num] = i
    return []

print(sum_of_two_nums([3,3],6))
print(sum_of_two_nums([2,7,23,56,78],9))
print(sum_of_two_nums([5,3,3,17,2,5],10))
