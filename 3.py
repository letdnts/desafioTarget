import json

def carregar_dados(arquivo):
    with open(arquivo, 'r') as file:
        dados = json.load(file)
    return dados

def calc_estatisticas(faturamento):
    valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

    if not valores:
        return None, None, 0

    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)

    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_da_media

def main():
    faturamento = carregar_dados('dados.json')  
    menor_valor, maior_valor, dias_acima_da_media = calc_estatisticas(faturamento)

    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

if _name_ == "_main_":
  main()
