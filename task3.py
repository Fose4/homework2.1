print ('Введите число координаты х:')
x = int(input())
print ('Введите число координаты y:')
y = int(input())

if x>0 and y>0:
    print(f"x = {x}; y = {y} -> 1")
elif x<0 and y>0:
    print(f"x = {x}; y = {y} -> 2")
elif x<0 and y<0:
    print(f"x = {x}; y = {y} -> 3")
elif x>0 and y<0:
    print(f"x = {x}; y = {y} -> 4")
elif x==0 and y==0:
    print("Значения не должны равняться нулю")
elif x==0 and y!=0:
    print("Точка находиться на оси Х")
elif x!=0 and y==0:
    print("Точка находиться на оси Y")