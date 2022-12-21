"""Creating a docstring"""
from typing import List


def send_invites(my_guest_list: List[str]):
    """Print out messages with invites to users whose names are in the provided list"""
    print(f"Proceeding to invite {len(my_guest_list)} people to dinner")
    for guest in my_guest_list:
        message = f"Dear {guest.title()} you are hereby invited to dinner!"
        print(message)


guest_list = ["bob ross", "bob cratchet", "sponge bob"]
send_invites(guest_list)

print(f"Oops, {guest_list[1].title()} cannot attend!")

guest_list[1] = "bob marley"

send_invites(guest_list)

print("We just found a bigger dinner table!!!")

guest_list.insert(0, "rick roll")
guest_list.insert((len(guest_list) // 2), "rick astley")
guest_list.append("happy gilmore")

send_invites(guest_list)


print("The new table won't arrive in time, only 2 guests can come!")

while len(guest_list) > 2:
    uninvited = guest_list.pop()
    print(f"Dear {uninvited.title()} unfortunately we don't have room for you anymore, sorry!")

send_invites(guest_list)

del guest_list[0]
del guest_list[0]

send_invites(guest_list)
