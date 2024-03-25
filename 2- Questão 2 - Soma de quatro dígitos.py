print('=-'*208)
print('ESSE PROGRAMA FAZ A SOMA DOS QUATRO DÍGITOS DE UM NÚMERO!')
n=int(input('Digite um número que contenha quatro dígitos: '))
# unidade:
a= n % 10
n= n // 10
# dezena
b= n % 10
n= n //10
# centena
c= n % 10
n= n//10
# milhar
d= n 
# soma
soma = a + b + c + d
print('A soma dos quatro dígitos desse número corresponde a: ',soma)