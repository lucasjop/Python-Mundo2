from datetime import date
print('{:-^40}'.format('Exercício 41'))
dataNascimento = str(input('Digite sua data de nascimento no formato dd/mm/aaaa: ')).strip()
anoAtual = date.today().year
anoNascimento = float(dataNascimento[6:])
idade = (anoAtual - anoNascimento)

if (idade <= 9):
    print('Categora MIRIM')
elif (idade <= 14):
    print('Categoria INFANTIL')
elif (idade <= 19):
    print('Categora JÚNIOR')
elif (idade <= 25):
    print('Categora SÊNIOR')
else:
    print('Categoria MASTER')