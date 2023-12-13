# def hello_world():
#     print("Hello World!")

# hello_world()

# def sum(num1=0, num2=0):
#     if type(num1) is not int or type(num2) is not int:
#         return 0
#     return num1 + num2

# total = sum(1, False)
# print(total)

def mutiple_items(*args):
    print(args)
    print(type(args))

mutiple_items("Dave", 40, "male")

def mutiple_named_items(**args):
    print(args)
    print(type(args))

mutiple_named_items(first = "Rick", last = "Yang")
