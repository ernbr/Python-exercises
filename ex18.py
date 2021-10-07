'''#18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). '''
######################################## ########################################

tamanho = int(input("Informe o tamanho do seu arquivo em MB: "))
velocidade = int(input("Informe a velocidade da sua conexao: "))

#Resultado em segundos
tempo_m = int((tamanho / (velocidade/8)) // 60)
tempo_s = int((tamanho / (velocidade/8)) % 60)

print (f'O tempo aproximado para download é de {tempo_m:2d} minutos e {tempo_s:2d} segundos ')

######################################## ########################################
#Resultado em segundos
  #Deve converter a velocidade Mb/s (Megabits por segundo) ou Kb/s (Kilobits por segundo) em Megabytes (MB).
  #Lembre-se, 8 bits equivalem a 1 byte, portanto, para calcular isso, é necessário dividi-lo por 8.
  #Portanto, nossa equação é: 5 Megabits por segundo / 8 = 0,625 Megabytes por segundo.
  #Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) =  tempo em segundos.
