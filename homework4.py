# immutable_var = 5, 'привет', 8, 'пока'
# print(immutable_var)
# immutable_var[0] = 9 # меняем значение первого элемента (5) на значение 9, в результате получаем ошибку
# print(immutable_var) # TypeError: 'tuple' object does not support item assignment поскольку кортеж не позволяет менять типы данных

mutable_list = ['один', 'два', 'три', 'четыре',]
print(mutable_list)
print(mutable_list[1])
mutable_list[1] = 'пять'
print(mutable_list)
