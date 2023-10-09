import json

while True:
    try:
        kod = int(input("Выберете задание или выберете 0 для выхода: "))
        match kod:
            case 1:
                try:
                    with open('F1.txt', 'w') as f1:
                        while True:
                            line = input("Введите строку (пустая строка для завершения ввода): ")
                            if line == '':
                                break
                            f1.write(line + '\n')
                except IOError:
                    print("Произошла ошибка ввода-вывода!")
                try:
                    with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
                        for line in f1:
                            if not any(char.isdigit() for char in line):
                                f2.write(line)
                except IOError:
                    print("Произошла ошибка ввода-вывода!")
                count = 0
                try:
                    with open('F2.txt', 'r') as f2:
                        for line in f2:
                            if line.startswith('A') or line.startswith('a'):
                                count += 1
                except IOError:
                    print("Произошла ошибка ввода-вывода!")
                print("Количество строк, начинающихся на букву 'А' в файле F2:", count)
            case 2:
                try:
                    with open('numbers.txt', 'r') as file, open('translated.txt', 'w+') as new_f:
                        for line in file:
                            if 'One' in line:
                                line = line.replace('One', 'Один')
                            if 'Two' in line:
                                line = line.replace('Two', 'Два')
                            if 'Three' in line:
                                line = line.replace('Three', 'Три')
                            if 'Four' in line:
                                line = line.replace('Four', 'Четыре')
                            new_f.write(line)
                        new_f.seek(0)
                        for line in new_f:
                            print(line, end="")
                except IOError:
                    print("Произошла ошибка ввода-вывода!")
            case 3:
                try:
                    subject_dict = {}

                    with open('subjects.txt', 'r', encoding='utf-8') as file:
                        for line in file:
                            parts = line.split(':')
                            subject = parts[0].strip()
                            lessons = parts[1].split()

                            total_lessons = 0
                            for lesson in lessons:
                                count, lesson_type = lesson.split('(')
                                total_lessons += int(count)
                            subject_dict[subject] = total_lessons
                    print(subject_dict)

                except IOError:
                    print("Произошла ошибка ввода-вывода!")
            case 4:
                try:
                    list = []
                    profits = []

                    with open('firms.txt', 'r') as file:
                        for line in file:
                            line = line.strip()
                            parts = line.split()
                            firm_name = parts[0]
                            ownership_form = parts[1]
                            revenue = int(parts[2])
                            expenses = int(parts[3])
                            profit = revenue - expenses

                            list.append({firm_name: abs(profit)})
                            if profit > 0:
                                profits.append(profit)

                    average_profit = int(sum(profits)/len(profits))
                    list.append({"average_profit": average_profit})

                    with open('firms.json', 'w') as file:
                        json.dump(list, file)
                    json_str = json.dumps(list)
                    print(json_str)
                except IOError:
                    print("Произошла ошибка ввода-вывода!")
            case 0:
                break
    except ValueError:
        print("Необходимо ввести натуральное число")
