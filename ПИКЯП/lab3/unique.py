class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)

        self.items = iter(items)

        self.seen = set()

        self.next_item = None

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            current = next(self.items)

            if self.ignore_case and isinstance(current, str):
                key = current.lower()
            else:
                key = current

            if key not in self.seen:
                self.seen.add(key)
                return current
print("Тест 1 - числа:")
data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
for item in Unique(data1):
    print(item, end=" ")
print()

print("\nТест 2 - генератор:")
from gen_random import gen_random
data2 = gen_random(10, 1, 3)
for item in Unique(data2):
    print(item, end=" ")
print()

print("\nТест 3 - строки (ignore_case=False):")
data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
for item in Unique(data3):
    print(item, end=" ")
print()

print("\nТест 4 - строки (ignore_case=True):")
data4 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
for item in Unique(data4, ignore_case=True):
    print(item, end=" ")
print()

print("\nТест 5 - смешанные данные:")
data5 = [1, '1', 1, '1', 'a', 'A', 2, '2']
for item in Unique(data5):
    print(item, end=" ")
print()

print("\nТест 6 - смешанные данные с ignore_case=True:")
data6 = [1, '1', 1, '1', 'a', 'A', 2, '2']
for item in Unique(data6, ignore_case=True):
    print(item, end=" ")
print()  
