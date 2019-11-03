with open('mensagem.txt', 'r') as file:
    data = file.readlines()

print(data)
data[4] = 'Linha5\n' 

with open('mensagem.txt', 'w') as file:
    file.writelines( data )

print('-------------')
print(data)