def get_gcd(num_1, num_2):
    if num_2 == 0:
        return num_1
    else:
        return get_gcd(num_2, num_1 % num_2)

# для проверки задания 1
# # num_1, num_2 = (int(input()), int(input()))
# # call_num = get_gcd(num_1, num_2)
# # print(f"Число НОД с использованием рекурсии: {call_num}")