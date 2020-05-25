from scipy.stats import norm

# Conjunto de objetos em uma cesta, a media é 8 e o desvio padrao é 2
# Qual a probabilidade de tirar um objeto que o peso é menor que 6 quilos?
norm.cdf(6, 8, 2)  #cdf = funcao para maior

#Qual a probabilidade de tirar um objeto que o peso é maior que 6 quilos?
norm.sf(6, 8, 2) #sf = funcao para menor

# Qual a probabilidade de tirar um objeto que o peso é menor que 6 ou maior
# que 10 quilo?
norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)

# Qual a probabilidade de tirar um objeto que o peso é menor que 10 e maior
# que 8 quilos?
norm.cdf*(10, 8, 2) - norm.cdf(8, 8, 2)




