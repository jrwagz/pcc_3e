for iter in range(1, 21):
    print(iter)

print(list(range(1, 21)))

very_long_list = [iter for iter in range(1, 1_000_001)]
# for value in very_long_list:
#     print(value)

print(min(very_long_list))
print(max(very_long_list))
print(len(very_long_list))
print(sum(very_long_list))


odd_numbers = list(range(1, 20, 2))
for number in odd_numbers:
    print(number)

multiples_of_three = [number for number in range(3, 31, 3)]
for value in multiples_of_three:
    print(value)

cubes = [number**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)


print("The first three items in the list are:")
for number in very_long_list[:3]:
    print(f"\t{number}")


print("The middle three items in the list are:")
middle_index = (len(very_long_list) // 2) - 2
for number in very_long_list[middle_index : middle_index + 3]:
    print(f"\t{number}")


print("The last three items in the list are:")
for number in very_long_list[-3:]:
    print(f"\t{number}")
