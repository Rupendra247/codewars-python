def rental_car_cost(d):
    r = 40
    t = d * r
    if d >= 3 and d < 7:
        return t - 20 
    elif d >= 7:
        return t - 50 
    elif d < 3:
        return 40
    else:
        return 0