#jogo do bicho!
print('Jogo do Bicho!!');

#importações
import random
import time


#regras
print('''
REGRAS:
O Jogo do bicho é um jogo de aposta e escolha.
1 - Você escolhe um dos bichos.
2 - O sorteio é realizado pelo computador.
3 - O resultado sai logo em seguida.
''');

#Variável externa
max_tentativa = False;
t = 4;

#Opção de jogo
while True:
        
    print('''
Qual dos bichos você escolhe?
[1] - Leão
[2] - Tigre
[3] - Coelho
[4] - Burro
    ''')
    opcao = int(input('Qual animal você escolhe: '));

    if opcao > 4 or opcao == 0:
        t = t-1
        time.sleep(1)
        print('\n');
        print(f'Opção Inválida, tente novamente.\nVocê possui {t} tentativas');
        print('\n');
        if t == 0:
            print('Você excedeu a quantidadade de tentativas.');
            print('\n');
            max_tentativa = True;
            break;

    #Variáveis e Lista
    sorteio = random.randint(0,3);
    lista_bicho = ['Leão', 'Tigre', 'Coelho', 'Burro'];

    time.sleep(1)

    # Leão
    if opcao == 1:
        print(f'Você escolheu: {lista_bicho[0]}');
        if sorteio == 0:
            time.sleep(1)
            print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
            print('Você acertou!!!');
            time.sleep(1)
        else:
            time.sleep(1)
            print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
            print('Você errou. Mais sorte na proxima');
            time.sleep(1)


    # Tigre
    if opcao == 2:
        print(f'Você escolheu: {lista_bicho[1]}');
        if sorteio == 1:
            time.sleep(1)
            print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
            print('Você acertou!!!');
            time.sleep(1)
        else:
            time.sleep(1)
            print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
            print('Você errou. Mais sorte na proxima');
            time.sleep(1)

    #Coelho
    if opcao == 3:
        print(f'Você escolheu: {lista_bicho[2]}');
        if sorteio == 2:
            time.sleep(1)
            print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
            print('Você acertou!!!');
            time.sleep(1)
        else:
            time.sleep(1)
            print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
            print('Você errou. Mais sorte na proxima');
            time.sleep(1)
            
    #Burro
    if opcao == 4:
        print(f'Você escolheu: {lista_bicho[3]}');
        if sorteio == 3:
            time.sleep(1)
            print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
            print('Você acertou!!!');
            time.sleep(1)
        else:
            time.sleep(1)
            print(f'O bicho sorteado foi: {lista_bicho[sorteio]}');
            print('Você errou. Mais sorte na proxima');
            time.sleep(1)
