produkts = []
print()
print('Заполните карточки товаров')
i = 0
while i < 3:
    i += 1
    staff = (i, {'name': input('name: '), 'cost': float(input('cost: '))})
    produkts.append(staff)

# -----Аналитика---------
print()
print('-' * 50)
print('Names: ', end='')
for i, _staff in enumerate(produkts):
    print('%12s' % _staff[1].get('name'), ' ', end='')
print()
print('Costs: ', end='')
for i, _staff in enumerate(produkts):
    print('%12s' % _staff[1].get('cost'), ' ', end='')
print()
print('   Id: ', end='')
for i, _staff in enumerate(produkts):
    print('%12d' % i, ' ', end='')
print()
print('-' * 50)
print()
