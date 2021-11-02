'''
#46 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes.

Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e
depois calcular a média).

Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução,
portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

    Atleta: Rodrigo Curvêllo

    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m

    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.9 m

    Resultado final:
    Rodrigo Curvêllo: 5.9 m
'''
#lista atletas
atletas = []

while True:
    nome = input('Informe o nome do atleta: ')

    if nome == '': #se não digitar nome o programa encerra
        break

    # Cria um dicionario dentro da lista e assim coloca atributos dentro dele
    atleta = {'nome': nome, 'salto': [], 'media_salto':0, 'melhor_salto':0, 'pior_salto':0,}

    #irá solicitar 5 saltos e irá incluir no dicionario "atleta".
    for i in range (1,6):
        atleta.get('salto').append(float(input(f'Informe a distancia do %iº salto registrado: '%i)))

    #imprime o Nome e as posições dos saltos
    print(f'Nome: {nome}')
    print(f'Primeiro Salto: {atleta.get("salto")[0]} m\n'
          f'Segundo Salto:  {atleta.get("salto")[1]} m\n'
          f'Terceiro Salto:  {atleta.get("salto")[2]} m\n'
          f'Quarto Salto:  {atleta.get("salto")[3]} m\n'
          f'Quinto Salto:  {atleta.get("salto")[4]} m\n')

    # Irá ordenar a lista de saltos dentro do dicionario
    atleta.get('salto').sort()

    #Para a posição 0, seria o pior salto, assim ele retornar e armazena em pior salto esse valor e exclui da lista
    atleta['pior_salto'] = atleta.get('salto').pop(0)

    # Para a posição vazia, seria a ultima posicao da lista ordenada,
    # assim ele retornar e armazena em melhor salto esse valor e exclui da lista.
    atleta['melhor_salto'] = atleta.get('salto').pop()

    #A media dos saltos, é a soma dos 3 demais divido por 3
    atleta['media'] = sum(atleta.get('salto')) / 3

    print(f'Melhor salto: {atleta.get("melhor_salto"):.1f} m\n'
          f'pior salto: {atleta.get("pior_salto"):.1f} m\n'
          f'Média dos demais saltos: {atleta.get("media"):.1f} m\n'
          )
    atletas.append(atleta)

#Irá mostrar os resultados de todos os atletas
print ('Resultado Final')

for atleta in atletas:
    print(f'{atleta.get("nome")}: {atleta.get("media"):.1f} m')
