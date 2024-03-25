import math

print('=-'*208)
print('LEITURA DOS LADOS DE UM TRINAGULO')
print('ESSE PROGRAMA IDENTIFICA E DETERMINA SE OS LADOS DIGITADOS PELO USUÁRIO CORRESPONDEM A UM TRIANGULO E QUAL CLASSIFICAÇAÕ LHE É ATRIBUÍDA!')
a=float(input('Digite um valor para o lado a: '))
b=float(input('Digite um valor para o lado b: '))
c= float(input('Digite um valor para o lado c: '))
# condição 1- Identificar se os lados podem formar ou não um triangulo
x= b - c
m1= abs(x)
y= a - c
m2= abs (y)
z= a - b
m3= abs (z)
if x < a < b + c: 
    print('Os lados digitados obedecendo a regra matemática de (b-c) < a < b + c, os lados digitados podem formar um triangulo!')
elif y < b < a + c: 
    print('Os lados digitados obedecendo a regra matemática de (a-c) < b < a + c, os lados digitados podem formar um triangulo!')
elif z < c < a + b:
    print('Os lados digitados obedecendo  regra matemática de (a-b) < b < a + c, os lados digitados podem formar um triangulo!')
else: 
    h= bool
    h == False
    h=('Os lados digitados, por não obedecerem os princípios matemáticos anteriores, não podem formar um triangulo!')
    print(h)
# condição 2- Classificação de triangulos
if a == b and b == c and a == c: 
        print('Os valores atribuidos aos lados formam um triangulo!')
        print('Obedecendo o princípio matemática que afirma: a=b, b=c e a=c, os valores correspodentes aos lados formarão um triangulo equilátero!')
elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('Os valores atribuidos aos lados formarão um triangulo!')
        print('Obedecendo o princípio matemático que afirma: a= b com a != b, os valores correspondentes aos lados formarão um triangulo isóceles!')
elif h== True and a != b and a != c or b != c and h== True:
        print('O valores atribuidos aos lados formarão um triangulo!')
        print('Obedecendo o princípio matemática que afirma: a != b, a != c e b != c, os valores correspondentes aos lados formarão um triangulo escaleno!')
print('=-'*208)
# Aaron Goldberg - 20241014050033
# Jordan Julio - 20241014050014