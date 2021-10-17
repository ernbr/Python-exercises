'''
#27 - Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos
'''
turma = int(input('Informe a quantidade de turmas:'))
count=0
total_alunos = 0
while count < turma:
    count+=1
    alunos = int(input('Informe a quantidade de alunos por turma %d:'%count))
    while alunos > 40:
        alunos = int(input('Informe a quantidade de alunos por turma, uma turma não pode ter mais de 40 alunos:'))
    total_alunos+=alunos

media = total_alunos/turma
print(f'A escola possui cerca de {total_alunos} alunos.')
print(f'A média de alunos por turma é de {media}')
