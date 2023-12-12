users = ["Rick", "Eda", "Polly"]

data = ["Rick", 26, True]

emptylist= []

print("Is Rick a user in our system?")
print("Rick" in users)

print(users[1])
print(users[-2])

print(users.index("Rick"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(users))

users.append("Elsa")
print(users)

users += ["Jason"]
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Robert", "GPT"]
print(users)

users.remove("Bob")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ["dave"]
print(users)
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy1 = nums.copy()
numscopy2 = list(nums)
numscopy3 = nums[:]

numscopy1.sort()
numscopy2.sort()
numscopy3.sort(reverse=True)

print(numscopy1)
print(numscopy2)
print(numscopy3)
print(nums)

# Tuples
mytuple = tuple((2, 3, 36, 29, "Rick", 3, 3, 3))
anothertuple = ("Rick", 26, "male")
print(mytuple)
print(anothertuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = mytuple
print(one)
print(two)
print(hey)

print(mytuple.count(3))