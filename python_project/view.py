import Note


def create_note(number):
    title = check_length(
        input('Введите название заметки: '), number)
    body = check_length(
        input('Введите описание заметки: '), number)
    return Note.Note(title=title, body=body)


def start_board():
    print("\nПрограмма 'Заметки' и набор возможных действий:\n\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - поиск заметок по дате\n6 - показать заметку по её номеру id\n7 - выход\n\nВведите номер действия: ")


def check_length(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def exit():
    print("Вы закончили работу и вышли из программы! ")
