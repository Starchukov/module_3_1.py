#Создать переменную calls = 0 вне функций.
call = 0
#Функция count_calls подсчитывающая вызовы остальных функций (call += 1).
def count_calls ():#Создать функцию count_calls и изменять в ней значение переменной calls.
    global call
    call += 1

def string_info (string):#Создать функцию string_info с параметром string и реализовать логику работы по описанию.
    count_calls()
    return (len(string), string.upper(), string.lower())
#Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def is_contains (string, list_to_search):
    count_calls()
    return string.lower() in [string.lower() for string in list_to_search]
#Для функции is_contains лучше привести и искомую строку и все строки в списке в один регистр.
#strimg.lower or string.upper
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(call)