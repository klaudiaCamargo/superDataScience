from scipy.stats import binom

# Jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?
probi = binom.pmf(3, 5, 0.5)


# Passar por 4 sinais de 4 tempos(4 ruas no cruzamento = 0.25), qual a probabilidade de pegar sinal verde
# 0,1,2,3 ou 4 vezes seguidas?
probi_0 = binom.pmf(0, 4, 0.25)
probi_1 = binom.pmf(1, 4, 0.25)
probi_2 = binom.pmf(2, 4, 0.25)
probi_3 = binom.pmf(3, 4, 0.25)
probi_4 = binom.pmf(4, 4, 0.25)

# E se forem sinais de dois tempos(2 ruas = 0.5)?
probi_dois_tempos = binom.pmf(4, 4, 0.5)

# Probabilidade acumulativa
acumulativa = binom.cdf(4, 4, 0.25)

# Concurso de 12 questoes, qual a probabilidade de acertar 7 questoes considerando
# que cada questao tem 4 alternativas?
probi_sete_acertos = binom.pmf(7, 12, 0.25)





