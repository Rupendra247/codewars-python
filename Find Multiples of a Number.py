def find_multiples(integer, limit):
    # Your code here!
    multiples = []
    for integer in range(integer, limit + 1 , integer):
        multiples.append(integer)
    return multiples