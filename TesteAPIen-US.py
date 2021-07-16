import requests
import os
from random import *
from num2words import num2words

arquivo = os.path.abspath(os.getcwd())

def escreveNum(num):
    result = num2words(numero_testado)

    x = (str(numero_testado))
    

    if numero_testado > -1:
        x = x[2:]
        
        if x == '00':           
            result = result.replace("mil", "mil e")
    else:
        x = x[3:]
        
        if x == '00':           
            result = result.replace("mil", "mil e")

    return result

print('#############')
print('##INICIANDO CONSULTAS##')
print('#############')

numero_de_testes = 0
numero_de_testes_aprovados = 0
numero_de_testes_reprovados = 0

## NÚMERO DE TESTES A SEREM REALIZADOS
testes_a_realizar = 100


for i in range(testes_a_realizar):
    numero_testado = randint(-20000, 20000)
    try:
        request = requests.get('http://challengeqa.staging.devmuch.io/en/{}'.format(numero_testado))
        request_data = request.json()
        resultado_esperado = escreveNum(numero_testado)

        teste_resposta_resultado = request_data['full']
        teste_resposta_api_200 = '<Response [200]>'
        teste_resposta_api_400 = '<Response [400]>'

        if (numero_testado < 10001) and (numero_testado > -10001):

            ### TRATAMENTO DENTRO DO INTERVALO ACEITÁVEL ###
            ### TRATAMENTO DENTRO DO INTERVALO ACEITÁVEL ###

            if teste_resposta_resultado == resultado_esperado and (str(teste_resposta_api_200) == str(request)):
                numero_de_testes += 1
                numero_de_testes_aprovados += 1
                print('/n' *3)
                print('#############')
                print('Teste número {}'.format(numero_de_testes))
                print('#############')
                print('Número Testado: {}'.format(numero_testado))
                print('Resultado Esperado: {}'.format(resultado_esperado))
                print('Resposta do servidor: {}'.format(request))
                print('Resultado da Consulta: {}'.format(
                    request_data['full']))
                print('#############')
                print('###############')
                print('## TESTE APROVADO! ##')
                print('###############')
                print('Testes aprovados:{}'.format(numero_de_testes_aprovados))
                print('Testes reprovados:{}'.format(
                    numero_de_testes_reprovados))
                print('\n' * 3)

            elif teste_resposta_api_200 != str(request):
                numero_de_testes += 1
                numero_de_testes_reprovados += 1
                print('##############\n' * 2)
                print('TESTE COM PROBLEMA, RESULTADO NÃO ESPERADO ACONTECEU\n')
                print('##############\n' * 2)
                print('REQUEST DEVERIA SER: {}, PORÉM RETORNOU: {}\n'.format(
                    teste_resposta_api_400, request))
                print('Testes aprovados:{}\n'.format(numero_de_testes_aprovados))
                print('Testes reprovados:{}\n'.format(
                    numero_de_testes_reprovados))
                print('\n' * 3)

            elif teste_resposta_resultado != resultado_esperado:
                numero_de_testes += 1
                numero_de_testes_reprovados += 1
                print('##############\n' * 2)
                print('TESTE COM PROBLEMA, RESULTADO NÃO ESPERADO ACONTECEU\n')
                print('Numero testado:{}\n'.format(numero_testado))
                print('##############\n' * 2)
                retorno = (
                    f'O NÚMERO DEVERIA SER: {resultado_esperado}, PORÉM RETORNOU: {teste_resposta_resultado}')
                print(retorno)
                print('Testes aprovados:{}'.format(numero_de_testes_aprovados))
                print('Testes reprovados:{}'.format(
                    numero_de_testes_reprovados))
                print('\n' * 3)

                with open(arquivo+"/errosen-US.txt", "a") as file:
                    file.write("%s\n" % retorno)

            else:
                print('#############')
                print('Número Testado: {}'.format(numero_testado))
                print('Resultado Esperado: {}'.format(resultado_esperado))
                print('Resposta do servidor: {}'.format(request))
                print('Resultado da Consulta: {}'.format(
                    request_data['full']))
                print('#############')
                print('###############')
                print('### PROBLEMA IDENTIFICADO ###')
                print('###############')
                numero_de_testes += 1
                numero_de_testes_reprovados += 1
                print('Testes aprovados:{}'.format(numero_de_testes_aprovados))
                print('Testes reprovados:{}'.format(
                    numero_de_testes_reprovados))
                print('\n' * 3)

            ### TRATAMENTO DENTRO DO INTERVALO ACEITÁVEL ###
            ### TRATAMENTO DENTRO DO INTERVALO ACEITÁVEL ###

        elif teste_resposta_resultado == 'Invalid data' and str(request) == str(teste_resposta_api_400):
            numero_de_testes += 1
            numero_de_testes_aprovados += 1
            print('#############')
            print('Teste número {}'.format(numero_de_testes))
            print('#############')
            print('Número Testado: {}'.format(numero_testado))
            print('Resultado Esperado: {}'.format(resultado_esperado))
            print('Resposta do servidor: {}'.format(request))
            print('Resultado da Consulta: {}'.format(request_data['full']))
            print('###############')
            print('## TESTE APROVADO! ##')
            print(
                '## NÚMERO SELECIONADO FORA DO INTERVALO ## [-10.000 até 10.000] ##')
            print('###############')
            print('Testes aprovados:{}'.format(numero_de_testes_aprovados))
            print('Testes reprovados:{}'.format(numero_de_testes_reprovados))
            print('\n' * 3)

        elif teste_resposta_api_400 != str(request):
            numero_de_testes += 1
            numero_de_testes_reprovados += 1
            print('##############\n' * 2)
            print('TESTE COM PROBLEMA, RESULTADO NÃO ESPERADO ACONTECEU')
            print('##############\n' * 2)
            retorno = (
                    f'Número testado:{numero_testado} - O response deveria retornar: {teste_resposta_api_400}, PORÉM RETORNOU: {request}')
            print(retorno)
            print('Testes aprovados:{}'.format(numero_de_testes_aprovados))
            print('Testes reprovados:{}'.format(numero_de_testes_reprovados))
            print('\n' * 3)
            with open(arquivo+"/errosen-US.txt", "a") as file:
                    file.write("%s\n" % retorno)

        elif teste_resposta_resultado != 'Invalid data':
            numero_de_testes += 1
            numero_de_testes_reprovados += 1
            print('##############\n' * 2)
            print('TESTE COM PROBLEMA, RESULTADO NÃO ESPERADO ACONTECEU')
            print('##############\n' * 2)
            print('REQUEST DEVERIA SER: {}, PORÉM RETORNOU: {}'.format(
                'Invalid data', teste_resposta_resultado))
            print('Testes aprovados:{}'.format(numero_de_testes_aprovados))
            print('Testes reprovados:{}'.format(numero_de_testes_reprovados))
            print('\n' * 3)

    except:
        print('Requisição inválida... checar URL da API')

print('############################\n' * 4)
print('##### RESULTADO FINAL #####')
print('Número de Testes realizados: {}'.format(numero_de_testes))
print('Testes aprovados:{}'.format(numero_de_testes_aprovados))
print('Testes reprovados:{}'.format(numero_de_testes_reprovados))
print('############################\n' * 4)
percent_acerto = (numero_de_testes_aprovados/numero_de_testes)*100
print("O numéro de acertos foi de: {}%".format(percent_acerto))
percent_erro = (numero_de_testes_reprovados/numero_de_testes)*100
print("O numéro de erros foi de: {}%".format(percent_erro))
print('Foi gerado um arquivo com nome de erroen-US.txt para uma melhor análise dos erros apontados')
