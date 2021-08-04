# -*- coding: utf-8 -*-
"""
Created on Wed Aug 4 2021 10:58:28

@author: Jefferson
"""

"""
I = 1 
V = 5 
X = 10 
L = 50 
C = 100
D = 500
M = 100


if Algrom[-1] :
       proxima = Numeros_dic[Algrom[t+1]]
   else:
       proxima = 0
"""

Numeros_dic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000    
    }


while True:
    try:
       proxima=0
       x=0
       resultado = 0
       print("\n")
       acao = int(input("Converta Algarismos Romanos em Numeros Inteiros!!"
                        "\nPara ENTRAR escolha 1 | Para SAIR escolha 0\n")) 
       if acao == 1:
           Algrom = input("Entre com os algarismos: ")
           AlgaUP = Algrom.upper()
           ultimo = len(AlgaUP)
        
           for i in AlgaUP:
               atual = Numeros_dic[i]
               indice = x+1
           
               if indice < ultimo:
                   proxima = Numeros_dic[AlgaUP[indice]]
                   x=x+1
               else:
                   proxima = 0
               if atual >= proxima:
                   resultado = resultado + atual
               else:
                   resultado = resultado - atual
                   
           print("O Número correspondente é: ", resultado)
           
       elif acao == 0:
           break
       else:
           print("\n\n\nOpção Invalida!\n\n\n")
    except:
       print("\n\n\nEntrada Invalida!\n\n\n") 
            


    

    
    


