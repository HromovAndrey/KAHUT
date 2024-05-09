# Є словник з друзями де ключ людина а значення список друзів.
# Користувач вводить імена двох людей які є друзями повторює
# це певну кількість разів після чого дані зберігаються у файл
# Завантажте дані назад та виведіть на екран

import json
def app_friends(dictionary, name1, name2):
    if name1 not in dictionary:
        dictionary[name1] = []
    if name2 not in dictionary:
        dictionary[name2] = []

    dictionary[name1].append(name2)
    dictionary[name2].append(name1)

friends = {}
number_repetition = int(input("Введіть кількість повторень:"))

for _ in range(number_repetition):
    name1 = input("Введіть імя першої людини:")
    name2 = input("Введіть імя другої людиини:")
    app_friends(friends, name1, name2)

with open("friends.json", "w") as file:
     json.dump(friends, file)

with open("friends.json", "r") as file:
     friends = json.load(file)

print("Друзі:")
for name, list_friends in friends.items():
    print(f"{name}: {','.join(list_friends)}")