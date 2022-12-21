def get_gcd(num_1, num_2):
    if num_2 == 0:
        return num_1
    else:
        return get_gcd(num_2, num_1 % num_2)

# num_1, num_2 = (80, 100)
# call_num = get_gcd(num_1, num_2)
# print(f"Число НОД с использованием рекурсии: {call_num}")