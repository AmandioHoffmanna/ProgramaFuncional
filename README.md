# ProgramaFuncional
Trabalho 02 - Programação Funcional - Conversor de Moedas

Para rodar o código, basta ter o python instalado, acessar a pasta onde o arquivo esta através do terminal e execute o programa Conversao.py
No VSCODE, basta utilizar o atalho CTRL + SHIFT + D para abrir o debugger para rodar o código.

Funcionamento da aplicação:

O usuário insere o valor que deseja ser convertido, existe validações para certificar que o valor informado é valido para isso. Após é selecionado a moeda de origem e a moeda de destino, também exista validações para se certificar que as moedas sejam as mesmas disponíveis, caso contrário existe tratamento para avisar o usuário que ele não pode selecionar moedas indisponíveis e por fim o código imprime o resultado da conversão. No decorrer do código, foi comentado os principais pontos para deixar claro cada ação realizada nele.

Funções:

As funções puras no código, são para validar a entrada de dados(Valida_VlrEntrada) e a função que realiza a conversão dos valores(conversao).

O programa respeita a imutabilidade durante o processo de conversão, não modificando qualquer dado informado pelo usuário, apenas apresenta o valor final da conversão no final do programa.

A função de ordem superior(converter_lista_valores), aplica as conversões em uma lista de valores, funções que operam sobre outras funções.

Exemplo:

Valor de entrada: 100

Moeda de Origem: USD

Moeda de Destino: BRL

Saída: 579.00 BRL

DESENVOLVIDO POR: AMANDIO ARNOLDO HOFFMANN
