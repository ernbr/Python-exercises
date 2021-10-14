'''
#16 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500
'''
fib0=0
fib1=1

for i in range(0,90):
    i+=1
    num=fib0+fib1
    fib1=fib0
    fib0=num
    if num<500:
        print(num)
print('O proximo numero é maior que 500')

##############################
#ALTERNATIVA#
fib0=0
fib1=1
i=0
while i <90:
    i+=1
    num=fib0+fib1
    fib1 = fib0
    fib0 = num
    if num<500:
        print(num)
print('O proximo será maior que 500')
