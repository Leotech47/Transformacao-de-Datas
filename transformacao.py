# Recebe a entrada e armazena na variável "entrada"
entrada = input()

# Função responsável por converter as datas
def converter_datas(datas):
    # Separa as datas por ponto e vírgula
    lista_datas = datas.split(';')
    
    # Converte cada data para o formato "YYYY/MM/DD"
    datas_convertidas = []
    for data in lista_datas:
        dia, mes, ano = data.split('-')
        datas_convertidas.append(f"{ano}/{mes}/{dia}")
    
    return datas_convertidas

# Imprime a lista com as datas convertidas
print(converter_datas(entrada))
