'''
#15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''
fib0=0
fib1=1

for i in range(0,90):
    i+=1
    num=fib0+fib1
    print(num)
    fib1=fib0
    fib0=num

##############################
##ALTERNATIVA##
fib0=0
fib1=1
i=0
while i <90:
    i+=1
    num=fib0+fib1
    print(num)
    fib1 = fib0
    fib0 = num

