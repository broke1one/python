def task(value):
    if isinstance(value, list): #Если в функцию попадает список
        max_elem = max(value)
        print(f"Максимальный элемент списка - {max_elem}")
        value.remove(max_elem)
        print(value)
    elif isinstance(value, dict): #Если в функцию попдает словарь
        print("Словарь до сортировки:")
        for key in value:
            print(key, value[key])
        sorted_dict = sorted(value.items(), key = lambda item: item[1])
        print("Словарь после сортировки:")
        for key, value in sorted_dict:
            print(key, value)
    elif isinstance(value, int): #Если в функцию попадает число
        if value == 0:
            print(f"число которое вы ввели - {value}, оно не может быть простым")
        elif value < 0:
            print(f"Число которое вы ввели - {value}, отрицательные числа не простые")
        else:
            dividers = 1
            counter = 1
            while counter != value:
                if value % counter == 0:
                    dividers += 1
                counter += 1
            if dividers == 2:
                print(f"Число {value} простое")
            else:
                print(f"Число {value} не простое")
    elif isinstance(value, str): #Если в функцию попдает строка
        value = value.lower()
        vowels = "aeioаяуюоеёэиы"
        vowels_counter = 0
        consonants = "bcdfghjklmnqrstvwxyzбвгджзйклмнпрстфхцчшщ"
        consonants_counter = 0
        for i in value:
            if i in vowels:
                vowels_counter += 1
            elif i in consonants:
                consonants_counter += 1
            else:
                pass
        print(f"В строке находится {vowels_counter} гласных")
        print(f"В строке находится {consonants_counter} согласных")
            


while True:
    n = input("Что вы хотите создать?\n1 - Cписок\n2 - словарь\n3 - Число\n4 - Строка\n0 - ВЫход из программы\n")
    if n == "1":
        lst = list(map(int,input("Введите числовые значения списка:\n").split()))
        task(lst)
    elif n == "2":
        data = dict()
        while True:
            key = input("Введите ключ или 0 для выхода или task для выполнения сортировки: ")
            if key == "0":
                break
            elif key == "task":
                task(data)
            else:
                inf = input("Введите значение:")
                data[key] = inf

    elif n == "3":
        a = int(input("Введите число: "))
        task(a)
    elif n == "4":
        string = str(input("Введите строку: "))
        task(string)
    elif n == "0":
        print("До свидаиния")
        break
    else:
        print("Неверный выбор, попробуйте еще раз: ")
    


