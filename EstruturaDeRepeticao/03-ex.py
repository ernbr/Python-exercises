'''
#3 - Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
nome = input('Informe o seu nome: ')
while len(nome)<3:
        nome = input('Informe um nome válido: ')

idade = int(input('Informe a sua idade: '))
while idade <= 0 or idade >=150:
         idade = int(input('Informe uma idade válida: '))

salario = int(input('Informe o seu salario: '))
while salario <= 0:
         salario = int(input('Informe um salario válido: '))

sexo = input('Informe o seu sexo - F- feminino ou M- Masculino: ').lower()
print(sexo)
while sexo != 'f' and sexo !='m':
        sexo = input('Informe um sexo válido - F- feminino ou M- Masculino: ').lower()
        print(sexo)
if sexo=='f': sexo ='Feminino'
else: sexo='Maculino'

estado_civil = input('Informe a letra para o seu estado civil -(s)- solteiro, '
                     '(c)-casado, (v)-viuvo, (d)- divorciado; : ').lower()
while estado_civil != 's' and estado_civil != 'c'and estado_civil !='v'and estado_civil != 'd':
         estado_civil = input('estado civil invalido informe um estado civil válido- '
                              '-(s) - solteiro, (c)-casado, (v)-viuvo, (d)- divorciado; : ').lower()
if estado_civil == 's':
    estado_civil = 'Solteiro'
elif estado_civil == 'c':
    estado_civil = 'Casado'
elif estado_civil == 'v':
    estado_civil = 'Viuvo'
elif estado_civil == 'd':
    estado_civil = 'Divorciado'

print(f'O seus dados armazenados foram :Nome {nome}, idade: {idade}, salario: {salario}, '
      f'sexo: {sexo} e estado civil: {estado_civil}')
