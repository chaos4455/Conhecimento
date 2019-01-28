#exemplos do uso de strings



"""
#strings literais entre "" ou ''
a = "honda"
b = ' s2000'
print(a + b)

"""


"""
#imprimindo exelementos especificos da string 

#variavel a que representa um valor do tipo inteiro

a = str("honda")
#imprime a posição 0 da variavel a do tipo str

print(a[0])

"""


"""
#imprime intervalo especifico dentro de uma string
a = "hondas2000"
print(a[5:10])

"""


"""
#exemplo aplicação método .strip() #remove espaços
a = "1 2 3 6 4 5 6 5 4 6 6" 
print(a.strip())

"""

"""
#exemplo uso método len - conta o tamanho de uma string
a = "casa"
print(len(a))


"""


"""
#aplica lowercase para uma string

a = "CASA"
print(a.lower())

"""


"""
#exemplo aplica uppercase para string

r = "eclipse"
print(r.upper())

"""


"""
#exemplo uso método replace para troca de valor de uma string
r = "BRAZIL"
print(r.replace("Z", "S"))


"""

"""
#Exemplo de uso do método split para dividir strings a partir de um valor declarado ou nulo
a = " honda, s2000, 1999"
print(a.split(",")) #pode ser ())

"""

"""
#exemplo de uso do método input para definir uma variavel do tipo string
print("oi, diga seu nome")
nome = input()

print("bem vindo " + nome)
"""

