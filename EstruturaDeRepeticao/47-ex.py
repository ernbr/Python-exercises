'''
# 47 - Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. 
A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em 
sua apresentação e depois informe a sua média, conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

    # Atleta: Aparecido Parente
    # Nota: 9.9
    # Nota: 7.5
    # Nota: 9.5
    # Nota: 8.5
    # Nota: 9.0
    # Nota: 8.5
    # Nota: 9.7
    # 
    # Resultado final:
    # Atleta: Aparecido Parente
    # Melhor nota: 9.9
    # Pior nota: 7.5
    # Média: 9,04
'''
#lista atletas
atletas = []

while True:
    nome = input('Informe o nome do atleta: ')

    if nome == '': #se não digitar nome o programa encerra
        break

    # Cria um dicionario dentro da lista e assim coloca atributos dentro dele
    atleta = {'nome': nome, 'nota': [], 'media_nota':0, 'melhor_nota':0, 'pior_nota':0,}

    #irá solicitar 5 saltos e irá incluir no dicionario "atleta".
    for i in range (1,8):
        atleta.get('nota').append(float(input(f'Informe a %iº nota: '%i)))

    #imprime o Nome e as posições dos saltos
    print(f'Nome: {nome}')
    print(f'Nota: {atleta.get("nota")[0]}\n'
          f'Nota:  {atleta.get("nota")[1]}\n'
          f'Nota:  {atleta.get("nota")[2]}\n'
          f'Nota:  {atleta.get("nota")[3]}\n'
          f'Nota:  {atleta.get("nota")[4]}\n'
          f'Nota:  {atleta.get("nota")[5]}\n'
          f'Nota:  {atleta.get("nota")[6]}\n')

    # Irá ordenar a lista de saltos dentro do dicionario
    atleta.get('nota').sort()

    #Para a posição 0, seria o pior salto, assim ele retornar e armazena em pior salto esse valor e exclui da lista
    atleta['pior_nota'] = atleta.get('nota').pop(0)

    # Para a posição vazia, seria a ultima posicao da lista ordenada,
    # assim ele retornar e armazena em melhor salto esse valor e exclui da lista.
    atleta['melhor_nota'] = atleta.get('nota').pop()

    #A media dos saltos, é a soma dos 3 demais divido por 3
    atleta['media'] = sum(atleta.get('nota')) / 5

    print(f'Melhor nota: {atleta.get("melhor_nota"):.1f} \n'
          f'pior nota: {atleta.get("pior_nota"):.1f} \n'
          f'Média das demais notas: {atleta.get("media"):.2f} \n'
          )
    atletas.append(atleta)

#Irá mostrar os resultados de todos os atletas
print ('Resultado Final')

for atleta in atletas:
    print(f'{atleta.get("nome")}: {atleta.get("media"):.2f}')
