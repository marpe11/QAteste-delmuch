![Alt Text](https://media.giphy.com/media/ihDkhpyQMZiwOBwI9Z/giphy.gif)

# Necessário para rodar os testes:

Pip3
Request 
Number2Word

Utilizando o instalador de pacotes python, o PIP, utilize os seguintes comandos

pip installs request
pip installs number2words

##########################

# Premissas do testes

Devemos verificar os retornos da API fornecida. Tanto o resultado em JSON quanto o Response.
Ao passar um número dentro do intervalo [-10000, 10000], deverá retornar o número escrito por extenso, e exibir uma mensagem de sucesso(Response 200)

O teste considerará falho quando QUALQUER UMA das premissas abaixo acontecer: 
    1. Retornar algo diferente de (Response 200) para números dentro do intervalo citado
    2. Retornar Response 200 para números de FORA do intervalo citado
    3. Não retornar Response 400 (ERRO) para números fora do intervalo citado
    4. Não retornar o texto 'invalid data' para números fora do intervalo citado
    5. Se o número por extenso possui algum erro ortográfico

############################

O número é sorteado aleatóriamente, há 50% de chance de cair em um número dentro do intervalo  e 50% de chance de cair um número fora do intervalo.


# Apontamentos

O teste irá rodar 100x em busca de algum erro, após seu término irá apresentar os resultados em tela, número de acertos e erros e a porcentagem de cada um.

O teste gera um arquivo chamado erro.txt e erroUS.txt que reúnem os erros encontrados nesse processo.

# Rápida Avaliação

API em pt-BR: Foi encontrado alguns erros gramáticais dentro da resposta: 'dezassete', 'dezanove' e 'dezasseis''. O número 10.000 está retornando ''then thousend''ao invés de dez mil. 


API em en-US: Está retornando o resultado errado nas consultas fora de intervalo, ao invés de retornar erro 400 está retornando erro 401.  


