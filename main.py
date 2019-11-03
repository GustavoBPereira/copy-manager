import sys

# text = sys.argv[1:]
# text = ' '.join(text)
# stringify

# arquivo = open('mensagem.txt', 'a')
# arquivo.write(text)
# arquivo.write('\n')

# arquivo.close()


def add_old(text):
    print(text)
    print()
    print(type(text))
    print()
    print(dir(text))
    return True


def add_current(text):
    with open('put_entry.txt', 'r') as file:
        data = file.readlines()

    for index ,line in enumerate(data):
        if line == '## Current copy\n':
            for search_index ,search_end in enumerate(data[index:]):
                if search_end == '## END CURRENT\n':
                    old_copy = data[index+1: search_index+1]
                    data[index+1: search_index+1] = []
                    add_old(old_copy)
                    break
            data[index+1] = '\n' + text + '\n\n'

    with open('put_entry.txt', 'w') as file:
        file.writelines(data)
    return True