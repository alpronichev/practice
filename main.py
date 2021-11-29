def square():
    a = float(input('Введите длину в футах: '))
    b = float(input('Введите ширину в футах: '))
    s = a * b
    SQFT_PER_ACRE = s / 43560
    print('Площадь равна', round(SQFT_PER_ACRE, 2), 'акр')


def final_speed():
    from math import sqrt
    v1 = 0
    a = 9.8
    d = float(input('Введите высоту: '))
    final_speed = sqrt((v1**2) + (2*a*d))
    print('Финальная скорость', round(final_speed, 2), 'м/c')



def decorator(func):
    def wrapper():
        print('Была вызвана функция', func.__name__)
        import time
        start_time = time.time()
        func()
        print('Время, затраченное на выполнение функции:', round(time.time()  - start_time, 5))
    return wrapper()


decorator(square)
decorator(final_speed)

