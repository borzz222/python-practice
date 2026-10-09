n = int(input())
is_prime = [True] * (n + 1)   # Шаг 0: все числа «простые»
is_prime[0] = is_prime[1] = False

for i in range(2, int(n ** 0.5) + 1):   # идём по числам 2, 3, 4 (до √n)
    if is_prime[i]:                      # если число не вычеркнуто, оно простое
        for j in range(2 * i, n + 1, i): # перебираем его кратные
            is_prime[j] = False          # и вычёркиваем их