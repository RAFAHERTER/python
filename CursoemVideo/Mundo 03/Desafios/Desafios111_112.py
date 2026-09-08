from Pasta_Desafios import moeda
from Pasta_Desafios import dados

v = dados.leiaDinheiro("Digite o valor: R$ ")
a = dados.leiaFloat('Digite o percentual de aumento: ') 
r = dados.leiaFloat('Digite o percentual de redução: ') 
moeda.resumo(v, a, r)
