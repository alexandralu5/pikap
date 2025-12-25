import random

def gen_random(num_count, begin, end):
    return (random.randint(begin, end) for _ in range(num_count))

print("5 случайных чисел от 1 до 3:")
for num in gen_random(5, 1, 3):
    print(num, end=" ")
print()

print("\n10 случайных чисел от 0 до 100:")
for num in gen_random(10, 0, 100):
    print(num, end=" ")
print()

numbers = list(gen_random(8, 10, 20))
print(f"\n8 случайных чисел от 10 до 20: {numbers}")
