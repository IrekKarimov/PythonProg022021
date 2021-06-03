"""
 PYAP.spring_21 4 лекция
"""
def A(*args):
    """
    Создайте функцию, которая принимает переменное количество аргументов
     и находит среднее арифметическое ненулевых из них.
    Обратите внимание на формат вывода
    1 2 3        --->   2
    2 0 0 2 2    --->   2
    2 0 2 1 1    --->   1.5
    """
    b1 = ["1","2"]
    b2 = [int(x) for x in b1]
    print(b2)
    a1 = [x for x in args if x > 0]
    print(a1)
    ar = sum(a1)/len(a1)
    if ar % 1 == 0:
        print(int(ar))
    else:
        print(ar)


def B(s):
    """ OK. Напишите функцию, которая будет возвращать самое длинное слово в предложении.
     Если найдено более одного слова, то функция возвращает первое.
     The Tower of London was built in the 15th century -> century"""

    s1 = s.split()
    ln = 0
    c = ""
    for ss in s1:
        if len(ss) > ln:
            ln = len(ss)
            c = ss

    return c

s = "The Tower of London was built in the 15th century"

A(2,0,2,1,1)
#print(B(s))
