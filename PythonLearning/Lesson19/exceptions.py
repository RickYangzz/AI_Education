
x = 2

class JustNotCoolException(Exception):
    pass

try:
    # print(x)
    # print("This is a nomal day.")
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
    # print(3 / 0)
    # raise Exception("It's a custom exception.")
    raise JustNotCoolException("It's just not cool, man.")

except ZeroDivisionError:
    print("Please do not devide by zero.")
except Exception as error:
    print(error)
else:
    print("No Error")
finally:
    print("I'm going to do something with or without exceptions.")