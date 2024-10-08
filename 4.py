# Defina os dados como um dicionário
faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcule o total de faturamento mensal
total_faturamento = sum(faturamento_mensal.values())

# Calcule o percentual de representação de cada estado
for estado, valor in faturamento_mensal.items():
    percentual = (valor / total_faturamento) * 100
    print(f'Estado: {estado} - Percentual de representação: {percentual:.2f}%')