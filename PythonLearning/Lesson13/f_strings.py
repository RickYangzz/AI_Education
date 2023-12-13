person = "Dave"
coins = 3

print(person + " has " + str(coins) + "coins left.\n")

message = "%s has %s coins left.\n" % (person, coins)
print(message)

message = "{} has {} coins left.\n".format(person, coins)
print(message)

message = "{person} has {coins} coins left.\n".format(person=person, coins=coins)
print(message)

player = {
    "person": "Rick",
    "coins": 5
}
message = "{person} has {coins} coins left.\n".format(**player)
print(message)

# f_Strings! this is the way.
message = f"{person} has {coins} coins left.\n"
print(message)

message = f"{person} has {3 * 5} coins left.\n"
print(message)

# You can pass formatting options
# https://www.w3schools.com/python/ref_string_format.asp
for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} devided by 4.25 is {num / 4.25:.2%}")
