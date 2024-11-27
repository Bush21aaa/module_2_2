first = int (input('Введите первое число: '))
second = int (input('Введите второе число: '))
third = int (input('Введите третье число: '))
#print(first)
#print(second)
#print(third)
if first==second and second==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:(print(0))