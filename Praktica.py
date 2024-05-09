# import json
#
#
# def save_friend_file(friend, go_file):
#     with open(go_file, 'w') as file:
#         json.dump(friend, file)
#
# def download_friend_file(go_file):
#     with open(go_file, 'r') as file:
#         return json.load(file)
# friend = {
#         'Оля': ['Іван', 'Петро'],
#         'Іван': ['Оля', 'Марія'],
#         'Петро': ['Оля', 'Іван', 'Анна'],
#         'Марія': ['Іван', 'Анна'],
#         'Анна': ['Петро', 'Марія']
#     }
#
# def bring_friends_on_screen(friend):
#     print("Друзі:")
#     for name  in friend.items():
#         print(f"{name}: {', '.join(friend)}")
#
# go_file = ('друзі.json')
#
# save_friend_file(friend, go_file)
#
# save_friend = download_friend_file(go_file)
#
# bring_friends_on_screen(save_friend)

