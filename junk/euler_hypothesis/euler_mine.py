
# (a**5 + b**5) + (c**5 + d**5) = e**5


fifth_powers = {x**5 for x in range(1, 151)}
sum_of_two_fifth_powers = {x + y for x in fifth_powers for y in fifth_powers}


for a_plus_b in sum_of_two_fifth_powers:
    for c_plus_d in sum_of_two_fifth_powers:
        if a_plus_b + c_plus_d in fifth_powers:
            print(a_plus_b, c_plus_d)

