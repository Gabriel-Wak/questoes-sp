import json

def calcular_estatisticas_de_vendas(dados_de_vendas):
    # Extrair os valores de vendas diárias dos dados JSON
    vendas_diarias = [venda['valor'] for venda in dados_de_vendas if venda['valor'] is not None]

    # Calcular os valores mínimos e máximos de vendas diárias
    min_vendas = min(vendas_diarias)
    max_vendas = max(vendas_diarias)

    # Calcular a média mensal, ignorando valores nulos
    media_vendas = sum(vendas_diarias) / len(vendas_diarias)

    # Contar o número de dias com vendas acima da média mensal
    dias_acima_media = sum(1 for venda in vendas_diarias if venda > media_vendas)

    return {
        'min_vendas': min_vendas,
        'max_vendas': max_vendas,
        'dias_acima_media': dias_acima_media
    }

# Carregar os dados JSON de um arquivo (substituir com o caminho do arquivo)
with open('3.json') as f:
    dados_de_vendas = json.load(f)

# Calcular as estatísticas de vendas
estatisticas = calcular_estatisticas_de_vendas(dados_de_vendas)

# Imprimir os resultados
print("Valor mínimo de vendas diárias:", estatisticas['min_vendas'])
print("Valor máximo de vendas diárias:", estatisticas['max_vendas'])
print("Número de dias acima da média:", estatisticas['dias_acima_media'])

