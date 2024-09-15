"""Bill Splitter"""

import random

msg_1 = "Enter the number of friends joining (including you):"
msg_2 = "Enter the name of every friend (including you), each on a new line:"
msg_3 = 'Do you want to use the "Who is lucky?" feature? Write Yes/No:'
friend_dict = {}

try:
    friend_count = int(input(msg_1 + "\n"))
    if friend_count > 1:
        print(msg_2)
        friend_list = [input() for _ in range(friend_count)]
        bill_value = int(input("Enter the total bill value:\n"))
        lucky_friend = input(msg_3 + "\n").lower()
        if lucky_friend != "yes":
            print("No one is going to be lucky")
            print(
                friend_dict.fromkeys(friend_list, round(bill_value / friend_count, 2))
            )
        else:
            lucky_friend = random.choice(friend_list)
            print(f"{lucky_friend} is the lucky one!")
            friend_dict = friend_dict.fromkeys(
                friend_list, round(bill_value / (friend_count - 1), 2)
            )
            friend_dict[lucky_friend] = 0
            print(friend_dict)

    else:
        print("No one is joining for the party")
except Exception:
    print("OMG, look at the manual first!")
