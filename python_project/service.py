import file_operation
import Note
import view

number = 5  # минимальное количество знаков, которое может быть в тексте заметки


def add():
    note = view.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Вы добавили заметку! ')


def show(text):
    flag = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            flag = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            flag = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            flag = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if flag == True:
        print('ни одной заметки не найдено! ')


def id_edit_del_show(text):
    id = input('Введите номер id заметки: ')
    array = file_operation.read_file()
    flag = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            flag = False
            if text == 'edit':
                note = view.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка была изменена! ')
            if text == 'del':
                array.remove(notes)
                print('Вы удалили заметку! ')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if flag == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_operation.write_file(array, 'a')
