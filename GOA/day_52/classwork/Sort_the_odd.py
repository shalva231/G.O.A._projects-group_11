def sort_array(source_array):
    odd_nums = []
    for num in source_array:
        if num % 2 != 0:
            odd_nums.append(num)
    odd_nums.sort(reverse=True)

    result = []
    for num in source_array:
        if num % 2 == 0:
            result.append(num)
        else:
            result.append(odd_nums.pop())

    return result