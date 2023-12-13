# dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())
print(type(band.values()))

# list all items
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)


# change items
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # tuple
print(band)

# delete and clear
band["drums"] = "Bonham"
print(band)
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2
# print(band2) # Error: "band2" is not defined

# Copy dictionaries

# band2 = band # create a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Rick"
# print(band)

band2 = band.copy()
band2["drums"] = "Rick"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
band3["singer"] = "Dave"
print(band)
print(band3)

# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)

# Sets
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums2))

# No duplicate allowed
nums = {1, 2, 2, 4}
print(nums)

# True is  a dupe of one, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# But you cannot refer to an element in the set with an index position or a key.
nums.add(8)
print(nums)

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# You can use update with lists, tuples, and dictionaries, too.
nums.update(band)
print(nums)

# Merge two sets to create a new set.
one = {1, 2, 3}
two = {6, 7, 8}

anewset = one.union(two)
print(anewset)
print(one)

# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {2, 3, 4, 5}
two = {4, 5, 6, 7}

one.symmetric_difference_update(two)
print(one)
