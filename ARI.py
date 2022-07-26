#!/bin/python3

import math
import os
import random
import re
import sys

sentence = input('Digite a frase aqui:')
def automated_readability_index(sentence):
    letras = len(sentence)
    letras_sem_espaco = letras - sentence.count(' ')
    print(f'Letras: {letras_sem_espaco}')
    print("-" * 30)
    palavras = len(sentence.split())
    print(f'Palavras: {palavras}')
    print("-" * 30)
    frase = re.split(r'[.!?]+', sentence)
    frase = len(frase)
    print(f'Frases: {frase}')
    print("-" * 30)
    print(f'{frase} frase, {palavras} palavras, {letras_sem_espaco} letras ')
    print("-" * 30)
    formula1 = 4.71 * letras_sem_espaco / palavras
    formula2 = 0.5 * palavras / frase
    resultado = formula1 + formula2 - 21.43
    arredondamento = math.ceil(resultado)
    print(f'Resultado: {resultado}')
    print(f'Resultado arredondado: {arredondamento}')
    if arredondamento > 14:
        arredondamento = 14
        print(f'O índice de legibilidade após aplicação de regra é: {arredondamento}')
  
    elif arredondamento < 0:
        arredondamento = 1
        print(f'O índice de legibilidade após aplicação de regra é: {arredondamento}')
       
    else:
        print(f'O índice de legibilidade após aplicação de regra é: {arredondamento}')
       


automated_readability_index(sentence)
