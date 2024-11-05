# Taxas de cambio(dicionario para armazenar valores a chave correspondente)
TAXAS_CAMBIO = {
    ('USD', 'EUR'): 0.92,
    ('EUR', 'USD'): 1.08,
    ('USD', 'BRL'): 5.79,
    ('BRL', 'USD'): 0.17,
    ('EUR', 'BRL'): 6.29,
    ('BRL', 'EUR'): 0.15
}

# Valida os valores inseridos
def Valida_VlrEntrada(valor):
    try:
        valor = float(valor)
        return valor > 0
    except ValueError:
        return False

# aplica o calculo da conversao
def conversao(valor, taxa):
    return valor * taxa
 
def programa_conversor():
    valor_entrada = input("Digite o valor que deseja converter: ")
    
    if not Valida_VlrEntrada(valor_entrada):
        print("Valor inválido. Insira um número positivo.")
        return

    valor_entrada = float(valor_entrada)

    # Exibe as moedas disponiveis
    #Busca por todas as moedas no TAXAS_CAMBIO do lado esquerdo e faz um union com o direuto para trazer todas as moedas sem repetir e salva em uma lista
    moedas = list({x[0] for x in TAXAS_CAMBIO.keys()}.union({x[1] for x in TAXAS_CAMBIO.keys()}))
    print("Moedas disponíveis:", ', '.join(moedas))

    moeda_origem = input("Escolha a moeda de origem: ").upper()
    moeda_destino = input("Escolha a moeda de destino: ").upper()

    # Tratamento para dar erro caso seja selecionado uma moeda inválida
    if (moeda_origem, moeda_destino) not in TAXAS_CAMBIO:
        print("Conversão não disponível para as moedas selecionadas.")
        return

    # busca a taxa do dicionpario
    taxa = TAXAS_CAMBIO[(moeda_origem, moeda_destino)]

    # Conversao
    valor_convertido = conversao(valor_entrada, taxa)
    print(f"{valor_entrada:.2f} {moeda_origem} é igual a {valor_convertido:.2f} {moeda_destino}.")

# Função de ordem superior para aplicar a conversão em uma lista de valores
def converter_lista_valores(valores, taxa):
    return list(map(lambda valor: conversao(valor, taxa), valores))

programa_conversor()
