from scipy.stats import t

# Média de salario dos cientistas de dados = R$ 75,00 por hora 
# Amostra com 9 funcionarios e desvio pdrao = 10

# Qual a probabilidade de selecionar um cientista de dados e o salario
# ser menor que R$ 80 por hora
a = t.cdf(1.5, 8)

#Qual a probabilidade do salario ser maior do que 80?
b = t.sf(1.5, 8) * 100

c = t.cdf(1.5, 8) + t.sf(1.5, 8)

d = 1 - t.cdf(1.5, 8)
