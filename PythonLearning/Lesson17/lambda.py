from functools import reduce

squared = lambda num: num * num
print(squared(4))

add_two = lambda num: num + 2
print(add_two(5))

sum_total = lambda a, b: a + b
print(sum_total(5,5))

################################

def func_builder(x):
    return lambda num: num + x

add_ten = func_builder(10)
add_twenty = func_builder(20)

print(add_ten(3))
print(add_twenty(6))

################################

numbers = [4, 5, 7, 12, 15, 25, 34]

squared_result = map(lambda num: num * num, numbers)

print(list(squared_result))

################################

odd_numbers = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_numbers))

################################

total = reduce(lambda accu, curr: accu + curr, numbers, 10)
print(total)
print(sum(numbers, 10))

names = ["Rick Yang", "Dave Gray", "Jason Jacob"]
char_count = reduce(lambda counter, current: counter + len(current), names, 0)
print(char_count)