def get_gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1

    print(num_1 + num_2)

get_gcd(100, 80) # Получение НОД методом деления
