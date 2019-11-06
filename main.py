from pyperclip import paste

my_file = 'copy_manager.txt'

def add_current(text):
    with open(my_file, 'r') as file:
        data = file.readlines()

    lines_old_copy =  get_position_old_copy(data)
    old_text = ''.join(data[lines_old_copy['start']: lines_old_copy['end']])
    clear_old_copy( data, lines_old_copy )

    with open(my_file, 'w') as file:
        data[lines_old_copy['start']] = '\n' + text + '\n\n'
        file.writelines(data)
    add_old(old_text)
    return True

def add_old(text):
    with open(my_file, 'r') as file:
        data = file.readlines()
    for index, line in enumerate(data):
        if line == '## END CURRENT\n':
            data[index+1] = '\n-- latest copies --\n' + text + '\n'
            break

    with open(my_file, 'w') as file:
        file.writelines(data)
    return True


def get_position_old_copy(data):
    for index, line in enumerate(data):
        if line == '## Current copy\n':
            for search_index ,search_end in enumerate(data[index:]):
                if search_end == '## END CURRENT\n':
                    return {'start': index+1, 'end': search_index+1}
                    break

def clear_old_copy(data, position):
    data[position['start']:position['end']] = []
    return True

if __name__ == "__main__":
    text = paste()
    add_current(text)