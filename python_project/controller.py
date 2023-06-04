import service as s
import view as v


def start_program():
    input_from_user = ''
    while input_from_user != '7':
        v.start_board()
        input_from_user = input().strip()
        if input_from_user == '1':
            s.show('all')
        if input_from_user == '2':
            s.add()
        if input_from_user == '3':
            s.show('all')
            s.id_edit_del_show('del')
        if input_from_user == '4':
            s.show('all')
            s.id_edit_del_show('edit')
        if input_from_user == '5':
            s.show('date')
        if input_from_user == '6':
            s.show('id')
            s.id_edit_del_show('show')
        if input_from_user == '7':
            v.exit()
            break
