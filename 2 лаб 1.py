import math


def int_checker(value):
   try:
       int(value)
       return True
   except ValueError:
       print("Введено не числовое значение")
       return False
       

def solve(a,b,c):
    d = int(b) ** 2  - 4 * int(a) * int(c)
    print(f"Дискриминант равен: {d}")
    if d > 0:
        x1 = (int(b) * -1 + math.sqrt(d)) / 2 * int(a)
        x2 = (int(b) * -1 - math.sqrt(d)) / 2 * int(a)
        if x1 > x2:
            print(f"Наименьший корень уравнения - {x1}\nНаибольший корень уравнения - {x2}")
        elif x1 < x2:
            print(f"Наименьший корень уравнения - {x1}\nНаибольший корень уравнения - {x2}")
        else:
            print(f"Корни равны:\n{x1}\n{x2}")
    elif d == 0:
        x = (int(b) * -1) / 2 
        print(x)
    else:
        print("Дискриминант меньше 0")


a = input("Введите a: ")
if not int_checker(a):
    exit()
b = input("Введите b: ")
if not int_checker(b):
    exit
c = input("Введите c: ")
if not int_checker(c):
    exit
    
solve(a,b,c)