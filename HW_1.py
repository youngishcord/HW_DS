import random

#from os import times_result
#from timeit import default_timer as timer
#
#def time_decorator(func):
#    def f(*args, **kwargs):
#        print("старт работы функции")
#        a = timer()
#        func(*args, **kwargs)
#        b = timer()
#        print("конец работы функции")
#        print(f"time = {b-a}")
#    return f

'''
Задание 1
Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:
'''
def word(word):
    if len(word)%2 == 0:
        return word[(len(word)//2)-1:(len(word)//2)+1]
    else: return word[len(word)//2]
#print(word("test"))
#print(word("teste"))


'''
Задание 2
Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз) и после первого нуля выводит сумму всех ранее введенных чисел.
'''
def sum_of_dig():
    c = 0
    while 1:
        a = int(input("введите число "))
        if a == 0:
            return c
        else:
            c += a
#print(sum_of_dig())

'''
Задание 3
Мы делаем  dating-сервиса, и у нас есть список парней и девушек.
Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки! 
Но мы не будем никого знакомить, если кто-то может остаться без пары:
'''
def pair(b, g):
    b = sorted(b)
    g = sorted(g)
    if len(b) != len(g):
        return print('Внимание кто то может остаться без пары')
    print('Идеальные пары')
    for i in range(len(b)):
        print(b[i], 'и', g[i])
boys = ['Peter','Alex','John','Arthur','Richard']
girls = ['Kate','Liza','Kira','Emma','Trisha']
#pair(boys, girls)


'''
Задание 4
У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период по странам (структура данных в примере). 
Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!) для каждой страны.
'''
def temperature(countries_temperature):
    for i in range(len(countries_temperature)):
        print(countries_temperature[i][0], "-", round(((sum(countries_temperature[i][1])/len(countries_temperature[i][1]))-32)*(5/9),1))
    return
countries_temperature = [
    ['Thailand', [75.2,77.,78.8,73.4,68,75.2,77]],
    ['Germany', [57.2,55.4,59,59,53.6]],
    ['Russia', [35.6,37.4,39.2,41,42.8,39.2,35.6]],
    ['Poland', [50,50,53.6,57.2,55.4,55.4]]
]
#temperature(countries_temperature)

'''
Задание 5
Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя (пример структуры данных приведен ниже). 
Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех пользователей.
'''
def gm(ids):
    b = []
    for a, k in ids.items():
        b += k
    return set(b)

ids = {
    'user1':[213,213,213,15,213],
    'user2':[54,54,119,119,119],
    'user3':[213,98,98,35]
}

#print(ids)
#print(gm(ids))


'''
Задание 6
Дана переменная, в которой хранится список поисковых запросов пользователя (пример структуры данных приведен ниже). 
Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.
'''
def users_queries(queries):
    q = dict()
    for i in range(len(queries)):
        key = (len(queries[i].split(' ')))
        if key not in q.keys():
            q.setdefault(key,1)
            #q[key] = 1
        else:
            a = {key: q[key] + 1}
            q.update(a)

    for k, v in q.items():
        print(f"Поисковых запросов, содержащих {k} слов(а): {round(((v/len(queries))*100),2)}%")    
    
    return 


queries = [
    "новости спорта",
    "афиша кино",
    "курс доллара",
    'смотреть сериалы онлан',
    "сериалы этим летом",
    "курс по питону",
    "сериалы про спорт"
]

def for_test():

    test = []

    for i in range(0, 10):
        j = random.randint(1,1000)
        test.append("слово " * j)
        test[i] = test[i][0:-1]
    return test

#users_queries(queries)
#users_queries(for_test())


'''
Задание 7
Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам. 
Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: (revenue / cost - 1) * 100
'''
def add_roi(data):
    for i in data.values():
        #print(i)
        roi = round(((i['revenue']/i['cost'])-1)*100,2)
        #print(roi)
        i.update({'ROI':roi})
    return data

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24}
}
#print(results.values())
#print(add_roi(results))


'''
Задание 8
Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж (пример структуры данных приведен ниже). 
Напишите программу, которая возвращает название канала с максимальным объемом продаж.
'''
def channel(stats):
    a = max(stats.items(), key=lambda x: x[1])
    print(f'Максимальный объем продаж на рекламном канале: {a[0]}')
    return a[0]

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

#channel(stats)