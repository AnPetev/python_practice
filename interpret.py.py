dict = {}
stack = []
# operations with variables
def load_value(variable):
    stack.append(variable)

def store_name(variable):
    val = stack.pop()
    dict[variable] = val

def load_name(variable):
    val = dict[name]
    stack.append(val)

def add_two_val(var1, var2):
    res = var1 + var2
    return res

def sub_two_val(var1, var2):
    res = var1 - var2
    return res

def print_val(variable):
    print(variable)

def increment(variable):
    variable += 1
    return variable

def decrement(variable):
    variable -= 1
    return variable

def mul(var1, var2):
    return var1 * var2

def div(var1, var2):
    return var1 * var2


def condition(cond, todo):
    if cond:
        return todo


