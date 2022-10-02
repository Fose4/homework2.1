print ('Введите день недели')
day = int(input())
if day < 1 or day >  7:
    print ('Введите корректный день недели')
elif day == 6 or day == 7:
    print (f'{day} -> да')
else: 
    print (f'{day} -> нет')
