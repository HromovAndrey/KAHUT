# Є словник з друзями де ключ людина а значення список друзів.
# Користувач вводить імена двох людей які є друзями повторює
# це певну кількість разів після чого дані зберігаються у файл
# Завантажте дані назад та виведіть на екран

import json
def app_friends(dictionary, name_1, name_2):
    if name_1 not in dictionary:
        dictionary[name_1] = []
    if name_2 not in dictionary:
        dictionary[name_2] = []

    dictionary[name_1].append(name_2)
    dictionary[name_2].append(name_1)

friends = []

number_repetition = int(input("Введіть кількість повторень:"))

for _ in range(number_repetition):
    name_1 = input("Введіть імя першої людини:")
    name_2 = input("Введіть імя другої людиини:")
    app_friends(friends, name_1, name_2)

with open("friends.json", "w") as file:
     json.dump(friends, file)

with open("friends.json", "r") as file:
     friends = json.load(file)

print("Друзі:")
for name, list_friends in friends.itemas():
    print(f"{name}: {','.join(list_friends)}")