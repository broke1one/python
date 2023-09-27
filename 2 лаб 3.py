def int_input(value):
    while True:
        try:
            int(value)
            return True
        except ValueError:
            print("Введено не числовое значение")
            return False
        finally:
            if int(value):
                print("Проврека завершена, значение числовое")
            else:
                print("Проверка завершена, значение не числовое")


def create_matrix(value):
   counter = 1
   if len(matrix) != 0:
       delete_matrix() 
   for i in range(n):
       matrix.append([])
       for j in range(n):
           element = input(f"Введите значение {counter} элемента")
           element = int(element)
           matrix[i].append(element)
           counter +=1


def view_matrix():
    if len(matrix) == 0:
        print("Матрица пустая, для начала создайте ее")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end = " ")
            print()


def delete_matrix():
   if len(matrix) == 0:
       print("Нельзя удалить пустую матрицу ")
   else:
       matrix.clear()
       print("Матрица очищена")


def task():
    counter = 0
    if len(matrix) == 0:
        print("Матрица пуста, для начала создайте ее")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    counter += 1
            if counter == n:
                print(f"Номер строки со всеми нулями - {i + 1}")
                for j in range(len(matrix[i])):
                    matrix[j][i] /= 2 
            counter = 0
            
                
matrix = []
print("Добро пожаловать!!!")
while True:
    print("1 - Создать матрицу\n2 - Просмотр матрицы\n3 - Удаление матрицы\n4 - Задание\n0-Выход из программы")
    choice = input("Выберите действие: ")
    if choice == "1":
        
        n = input("Введите размер матрицы n x n: ")
        if int_input(n):
            n = int(n)
            if n < 0:
                print("Размер матрицы не может быть отрицательным значением")
                break
            if n == 0:
                print("Размер матрицы не может быть равен нулю")
                break
            else:
                create_matrix(n)
    elif choice == "2":
        view_matrix()
    elif choice == "3":
        delete_matrix()
    elif choice == "4":
        task()
    elif choice == "0":
        print("До свидания!")
        break
    else:
        print("Неверный выбор, попробуйте еще")