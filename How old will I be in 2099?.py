# def calculate_age(year_of_birth, current_year):
#     if year_of_birth < current_year:
#         return f"You are {current_year - year_of_birth} years old."
#     elif year_of_birth > current_year:
#         return f"You will be born in {year_of_birth - current_year} years."
#     elif year_of_birth == current_year:
#         return "You were born this very year!"

def calculate_age(year_of_birth, current_year):
    if year_of_birth < current_year:
        diff = current_year - year_of_birth
        word = "year" if diff == 1 else "years"
        return f"You are {diff} {word} old."
        
    elif year_of_birth > current_year:
        diff = year_of_birth - current_year
        word = "year" if diff == 1 else "years"
        return f"You will be born in {diff} {word}."
        
    elif year_of_birth == current_year:
        return "You were born this very year!"
