#jogo do bicho!
print('Jogo do Bicho!!');

#importações
import random

#regras
print('''
REGRAS:
O Jogo do bicho é um jogo de aposta e escolha.
1 - Você escolhe um dos bichos.
2 - O sorteio é realizado pelo computador.
3 - O resultado sai logo em seguida.
''');


#Opção de jogo
print('''
Qual dos bichos você escolhe?
[1] - Leão
[2] - Tigre
[3] - Coelho
[4] - Burro
''')
opcao = int(input('Qual animal você escolhe: '));

if opcao == 1:
    opcao = 0;
elif opcao == 2:
    opcao = 1;
elif opcao == 3:
    opcao = 2;
elif opcao == 4:
    opcao = 3;
else:
    print('Opção inválida.');

#Variáveis e Lista
sorteio = random.randint(0,3);
lista_bicho = ['Leão', 'Tigre', 'Coelho', 'Burro'];


# Leão
if opcao == 0:
    print(f'Você escolheu: {lista_bicho[opcao]}');
    if sorteio == 0:
        print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
        print('Você acertou!!!');
    else:
        print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
        print('Você errou. Mais sorte na proxima');


# Tigre
if opcao == 1:
    print(f'Você escolheu: {lista_bicho[opcao]}');
    if sorteio == 1:
        print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
        print('Você acertou!!!');
    else:
        print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
        print('Você errou. Mais sorte na proxima');

#Coelho
if opcao == 2:
    print(f'Você escolheu: {lista_bicho[opcao]}');
    if sorteio == 2:
        print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
        print('Você acertou!!!');
    else:
        print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
        print('Você errou. Mais sorte na proxima');
        
#Burro
if opcao == 3:
    print(f'Você escolheu: {lista_bicho[opcao]}');
    if sorteio == 3:
        print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
        print('Você acertou!!!');
    else:
        print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
        print('Você errou. Mais sorte na proxima');
