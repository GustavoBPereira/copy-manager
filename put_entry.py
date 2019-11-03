with open('put_entry.txt', 'r') as file:
    data = file.readlines()

copied = input('write here>')

for index ,line in enumerate(data):
    if line == '## Current copy\n':
        for search_index ,search_end in enumerate(data[index:]):
            if search_end == '## END CURRENT\n':
                data[index+1: search_index+1] = []
                break

        data[index+1] = '\n' + copied + '\n\n'

with open('put_entry.txt', 'w') as file:
    file.writelines(data)
