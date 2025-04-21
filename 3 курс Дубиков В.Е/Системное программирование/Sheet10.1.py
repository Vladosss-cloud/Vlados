import random

def generate_random_numbers(count, min_val, max_val):
    """Генерирует и выводит заданное количество случайных чисел в заданном диапазоне."""
    for _ in range(count):
        print(random.uniform(min_val, max_val))

# a) 
print ("a) 8 случайных чисел от 0 до 1:")
generate_random_numbers(8, 0, 1)

# б) 
k = int(input("б) Введите значение k: "))
print (f"б) {k} случайных чисел от 0 до 1:")
generate_random_numbers(k, 0, 1)

# в) 
print ("в) 15 случайных чисел от 25 до 26:")
generate_random_numbers(15, 25, 26)

# г) 
print ("г) 20 случайных чисел от 0 до 15:")
generate_random_numbers(20, 0, 15)

# д) 
a = int(input("д) Введите значение a: "))
b = float(input("д) Введите значение b: "))
k = random.randint(1, a)
print (f"д) Случайное k = {k}")
print (f"д) {k} случайных чисел от 0 до {b}:")
generate_random_numbers(k, 0, b)

# е) 
print ("е) 10 случайных чисел от -40 до 40:")
generate_random_numbers(10, -40, 40)

# ж) 
m = int(input("ж) Введите значение m: "))
a = float(input("ж) Введите значение a: "))
b = float(input("ж) Введите значение b: "))
k = random.randint(1, m)
print (f"ж) Случайное k = {k}")
print (f"ж) {k} случайных чисел от {a} до {b}:")
generate_random_numbers(k, a, b)