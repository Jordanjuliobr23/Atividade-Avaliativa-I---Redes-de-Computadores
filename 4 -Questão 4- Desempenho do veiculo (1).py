import math 
print('=-'*108)
print('Desempenho do veículo em uma viagem: ')
n=str(input('Digite o modelo do veículo: '))
h1=float(input('Digite ao momento de saída do veículo [Hora e minuto]: '))
h2=float(input('Digite o momento de chegada do veículo ao destino [Hora e minuto]: '))
s=float(input('Digite os segundos em que o veículo esteve parado: '))
l=float(input('Por favor informe a quantidade de litros de combustível gasto em litros: '))
p=float(input('O preço do litro do combustível em R$: '))
d=float(input('Digite a distancia pecorrida em Km/h: '))
# operação de conversão Horas e minutos para segundos!
t1= (h1*3600) 
t2= (h2*3600) 
tf= (t1-t2) 
mdtf= abs(tf)  
# Operação velocidade média e velocidade média em movimento! 
#velocidade média global
vt= (t1-t2) + s # tempo total contando com a parada do veículo
vmg= vt//d 
#velocidade média em movimento
vs= (t1-t2) # tempo pecorrido em movimento
vmm= vs//d
mdvmg= abs(vmm)
mdvmm= abs(vmm)
# Operação o custo da viagem!
c= p * d 
# Operação para o desempenho do veículo!
dp1= d // l 
dp2= l // tf
mddp2= abs(dp2)
dp3= p/d 

print('Dados de um computador de bordo: ')
print( 'Apresentação do desempenho do veículo  ', n)
print('O tempo da viagem em segundos é  ', mdtf)
print('A velocidade média global do veículo Km/h durante a viagem foi  ',mdvmg )
print('A velocidade média em movimento do veículo Km/h durante a viagem foi  ',mdvmm )
print('O custo da viagem foi de R$',int(c))
print('O desempenho do carro na viagem foi: ') 
print('K/L: ',dp1)
print('L/H: ',mddp2)
print('R$/KM: ',dp3)
print('=-'*108)
