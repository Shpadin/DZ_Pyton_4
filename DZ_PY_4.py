
task = int(input('введите номер залачи от 1 до 5:'))
match task:
    case 1:
        # 1 Число с заданной точностью
        number = float(input('Введите число: '))
        d = float(input('введите разряд округления: '))
        def round_number(number, d):
            d = str(d).split('.')
            d = len(d[1])
            return round(number, d)
        print(round_number(number, d))
    case 2:
        number = int(input('введите число:  '))
        # 2 Простые множители
        def simple_multiplier(number):
            result = []
            i = 2
            while number > 1:
                if number % i == 0:
                    result.append(i)
                    number //= i
                else:
                    i += 1
            return result
        print(simple_multiplier(number))
    case 3:
        # 3 Неповторяющиеся элементы
        n = int(input('размер списка:  '))
        def duplicate_number(n):
            from random import randint
            list_numbers = [randint(1, 99) for _ in range(n)]
            print(list_numbers)
            i, j = 0, 0
            while i < len(list_numbers):
                flag = True
                while j < len(list_numbers):
                    if i != j and list_numbers[i] == list_numbers[j]:
                        del list_numbers[j]
                        flag = False
                    if j == len(list_numbers) - 1 and flag == False:
                        del list_numbers[i]
                    j += 1
                i += 1
            return list_numbers
        print(duplicate_number(n))
    case 4:
        k = int(input('Введите степень многочлена:  '))
        # 4 Степень многочдена
        def degree_of_number(k):
            from random import randrange
            for i in range(1, 3):
                file_lesson = open(u'C:/Users/ShpadinPYU/Desktop/example_' + str(i) + '.txt', 'w')
                file_lesson.write(f'{randrange(1, 99)}*x^{k} + {randrange(1, 99)}*x + {randrange(1, 99)} = 0')
                file_lesson.close
        print('файл создан: C:/Users/ShpadinPYU/Desktop/example_ ')    
    case 5:
            # 5 Сложение многочленов
        def addition_of_polynomials():
            from re import findall
            file_1 = open(u'C:/Users/ShpadinPYU/Desktop/example_1.txt', 'r')
            file_2 = open(u'C:/Users/ShpadinPYU/Desktop/example_2.txt', 'r')
            polynominals_1, polynominals_2 = file_1.read(), file_2.read()
            match_1 = findall(r'\d+', polynominals_1)
            result_1 = list(map(int, match_1))
            match_2 = findall(r'\d+', polynominals_2)
            result_2 = list(map(int, match_2))
            result = list(map(sum, zip(result_1, result_2)))
            result_file = open(u'C:/Users/ShpadinPYU/Desktop/result.txt', 'w')
            result_file.write(f'{result[0]}*x^{match_1[1]} + {result[2]}*x + {result[3]} = 0')
        
        addition_of_polynomials()
        print('файл c суммой многочленов создан: C:/Users/ShpadinPYU/Desktop/example_ ')   
