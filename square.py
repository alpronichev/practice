a = float(input('Введите длину в футах: '))
b = float(input('Введите ширину в футах: '))
s = a * b

SQFT_PER_ACRE = s / 43560

print('Площадь равна', round(SQFT_PER_ACRE, 2), 'акр')
