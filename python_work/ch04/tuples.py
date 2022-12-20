buffet_foods = ("steak", "ice cream", "mashed potatoes", "cake", "chicken")
for food in buffet_foods:
    print(food)

# buffet_foods[0] = "should_cause_error"

print("\nWe have a new menu!!!")

buffet_foods = (buffet_foods[0], "kale", buffet_foods[2], "salad", buffet_foods[4])
for food in buffet_foods:
    print(food)
