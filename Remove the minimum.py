def remove_smallest(numbers):
    if not numbers:
        return []
    minimum = min(numbers)
    working_number = numbers.copy()
    working_number.remove(minimum)
    return working_number
print(remove_smallest([1,2,3,4,5]))
print(remove_smallest([5,3,2,1,4]))
print(remove_smallest([2,2,1,2,1]))