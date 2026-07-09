def square_sum(numbers):
    #your code here
    total = 0 
    for number in numbers:
        total += number ** 2 
    return total
print(square_sum([1, 2, 2]))