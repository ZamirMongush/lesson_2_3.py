# #Глобальная
# a = 4
# b = 41
# def printer():
# # Локальная
#     global  a, b
#     a = 'Str'
#     b = 'Str 2'
#     d = 14
#     c = 32
#     print(d, c, "local")
#     print(a, b, "global")
#
# print(a, b)
# printer()
# print(a, b)
from pstats import count_calls

calls = 0
def count_calls ():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for item in list_to_search:
        if item.lower() == string:
            return True
    return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)






